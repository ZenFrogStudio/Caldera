"""Generate the Caldera Sans family (Light, Regular, Bold).

A clean, highly readable sans-serif for UI and body text: generous x-height,
open apertures, distinct I / l / 1 and O / 0, and even spacing.

Every glyph is described as centre-line strokes (lines and superelliptic
arcs).  The strokes are expanded with a slightly flattened pen (horizontals a
touch thinner than verticals), merged with Shapely, kerned, autohinted and
written to TrueType / WOFF2 with fontTools.

    pip install fonttools shapely brotli ttfautohint-py
    python fonts/src/build_font.py
"""
import math
import os

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from shapely import affinity
from shapely.geometry import LineString, Point, Polygon, box
from shapely.geometry.polygon import orient
from shapely.ops import unary_union

FAMILY = "Caldera Sans"
VERSION = "2.000"

# name, stroke weight (vertical stems), usWeightClass
WEIGHTS = [("Light", 46, 300), ("Regular", 78, 400), ("Bold", 118, 700)]

UPM = 1000
XH = 540          # x-height (tall, for legibility at small sizes)
CH = 720          # cap height
AS = 760          # ascender
DS = -210         # descender
OV = 11           # overshoot for round shapes
SE = 2.2          # superellipse exponent (2 = ellipse, higher = squarer)
CONTRAST = 0.9    # horizontal stroke thickness relative to vertical

# set per weight by set_weight()
W = H = SX = SB = R_DOT = None


def set_weight(w):
    """Configure the globals that every glyph drawing reads."""
    global W, H, SX, SB, R_DOT
    W = w
    H = w / 2
    SX = 0.93 + (w - 46) * 0.001      # heavier weights get a little wider
    SB = 0.90 + (w - 46) * 0.0008     # ...and a little more room
    R_DOT = max(31, w * 0.66)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


# ---------------------------------------------------------------- primitives
def arc(cx, cy, rx, ry, a0, a1, n=SE, step=1.5):
    """Superelliptic arc from angle a0 to a1 (degrees, either direction)."""
    count = max(2, int(abs(a1 - a0) / step) + 1)
    pts = []
    for i in range(count + 1):
        t = math.radians(a0 + (a1 - a0) * i / count)
        c, s = math.cos(t), math.sin(t)
        x = math.copysign(abs(c) ** (2 / n), c)
        y = math.copysign(abs(s) ** (2 / n), s)
        pts.append((cx + rx * x, cy + ry * y))
    return pts


def flat(*parts):
    pts = []
    for p in parts:
        seq = p if isinstance(p, list) else [p]
        for q in seq:
            if not pts or math.dist(pts[-1], q) > 1e-6:
                pts.append(q)
    return pts


def sx(p):
    return (p[0] * SX, p[1])


def pen(geom_fn, pts):
    """Expand with a flattened pen: squash y, buffer round, unsquash."""
    k = CONTRAST
    g = geom_fn([(x * SX, y / k) for x, y in pts])
    return affinity.scale(g, 1, k, origin=(0, 0))


def stroke(*parts, join="round", w=None):
    w = w or W
    return pen(lambda p: LineString(p).buffer(w / 2, cap_style="flat", join_style=join,
                                              mitre_limit=4.0, quad_segs=24), flat(*parts))


def seg(p0, p1, e0=0, e1=0, w=None):
    """Straight stroke, optionally extended past either end (for clipping)."""
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    a = (p0[0] - ux * e0, p0[1] - uy * e0)
    b = (p1[0] + ux * e1, p1[1] + uy * e1)
    return stroke(a, b, w=w)


def ring(cx, cy, rx, ry, n=SE):
    return pen(lambda p: Polygon(p).exterior.buffer(H, quad_segs=24),
               arc(cx, cy, rx, ry, 0, 360, n)[:-1])


def dot(x, y, r=None):
    return Point(x * SX, y).buffer(r or R_DOT, quad_segs=32)


def clip(g, x0=-2000, y0=-2000, x1=4000, y1=4000):
    return g.intersection(box(x0 * SX, y0, x1 * SX, y1))


def oval(cx, oh, ow, base=0):
    """Centre-line radii for a round shape of outer size ow x oh."""
    return cx, base + oh / 2 - OV, ow / 2 - H, oh / 2 - H


class Glyph:
    def __init__(self, lsb=60, rsb=None, adv=None):
        self.lsb, self.rsb, self.adv = lsb, (lsb if rsb is None else rsb), adv
        self.parts = []
        self.cut = None
        self.box = None

    def add(self, *g):
        self.parts.extend(g)
        return self

    def geometry(self):
        g = unary_union(self.parts).buffer(0)
        if self.box:
            g = clip(g, *self.box)
        if self.cut is not None:
            g = g.difference(affinity.scale(self.cut, SX, 1, origin=(0, 0)))
        return g


GLYPHS = {}


def glyph(ch, **kw):
    def deco(fn):
        GLYPHS[ch] = (fn, kw)
        return fn
    return deco


# ------------------------------------------------------------- lowercase
def bowl(cx, top=XH, ow=500):
    oh = top + 2 * OV
    return ring(cx, top / 2, ow / 2 - H, oh / 2 - H)


@glyph("o", lsb=44)
def g_o(g):
    g.add(bowl(250))


@glyph("c", lsb=44, rsb=34)
def g_c(g):
    rx, ry = 470 / 2 - H, (XH + 2 * OV) / 2 - H
    g.add(stroke(arc(235, XH / 2, rx, ry, 50, 310)))


@glyph("e", lsb=44)
def g_e(g):
    rx, ry = 490 / 2 - H, (XH + 2 * OV) / 2 - H
    cx, cy = 245, XH / 2
    g.add(stroke((cx - rx, cy + 4), (cx + rx, cy + 4)))
    g.add(stroke(arc(cx, cy, rx, ry, -8, 316)))


def s_shape(top, ow, mid_ratio=0.53):
    bot_c = H - OV
    top_c = top + OV - H
    mid = top * mid_ratio
    rxl = ow / 2 - H
    rxu = rxl - 16
    cx = ow / 2
    ryu = (top_c - mid) / 2
    ryl = (mid - bot_c) / 2
    cyu = mid + ryu
    cyl = mid - ryl
    up = arc(cx - 8, cyu, rxu, ryu, 28, 252)
    lo = arc(cx, cyl, rxl, ryl, 72, -150)
    return stroke(up, lo)


@glyph("s", lsb=44)
def g_s(g):
    g.add(s_shape(XH, 400))


def arch(L, R, top, ry=205, y0=0):
    cx, rx = (L + R) / 2, (R - L) / 2
    ya = top + OV / 2 - H - ry
    return stroke((R, y0), (R, ya), arc(cx, ya, rx, ry, 0, 180))


@glyph("n", lsb=64)
def g_n(g):
    L, R = H, 430 - H
    g.add(stroke((L, 0), (L, XH)), arch(L, R, XH))


@glyph("h", lsb=64)
def g_h(g):
    L, R = H, 430 - H
    g.add(stroke((L, 0), (L, AS)), arch(L, R, XH))


@glyph("m", lsb=64)
def g_m(g):
    L, M, R = H, 340, 680 - H
    g.add(stroke((L, 0), (L, XH)), arch(L, M, XH, 190), arch(M, R, XH, 190))


@glyph("u", lsb=64)
def g_u(g):
    L, R = H, 430 - H
    ry = 205
    cx, rx = (L + R) / 2, (R - L) / 2
    yb = H - OV / 2 + ry
    g.add(stroke((L, XH), (L, yb), arc(cx, yb, rx, ry, 180, 360)))
    g.add(stroke((R, XH), (R, 0)))


@glyph("r", lsb=64, rsb=20)
def g_r(g):
    L = H
    ry, rx = 215, 175
    ya = XH + OV / 2 - H - ry
    g.add(stroke((L, 0), (L, XH)), stroke(arc(L + rx, ya, rx, ry, 180, 72)))


@glyph("i", lsb=64)
def g_i(g):
    g.add(stroke((H, 0), (H, XH)), dot(H, XH + 95 + R_DOT))


@glyph("j", lsb=-10, rsb=64)
def g_j(g):
    x, r = 150, 120
    y0 = DS + H + r
    g.add(stroke((x, XH), (x, y0), arc(x - r, y0, r, r, 0, -90)))
    g.add(dot(x, XH + 95 + R_DOT))


@glyph("l", lsb=64, rsb=24)
def g_l(g):
    # a small tail keeps l distinct from I and 1
    r = 95
    y0 = H * CONTRAST - OV / 2 + r
    g.add(stroke((H, AS), (H, y0), arc(H + r, y0, r, r, 180, 272)))


@glyph("t", lsb=24, rsb=30)
def g_t(g):
    x, r = 120, 115
    top = 670
    y0 = H - OV / 2 + r
    g.add(stroke((x, top), (x, y0), arc(x + r, y0, r, r, 180, 275)))
    g.add(stroke((x - 110, XH - H), (x + 150, XH - H)))
    # sloped cut across the top of the stem
    g.cut = Polygon([(x - 60, top - 46), (x + 60, top + 4), (x + 60, 900), (x - 60, 900)])


@glyph("f", lsb=24, rsb=10)
def g_f(g):
    x, r = 130, 140
    y1 = AS + OV / 2 - H - r
    g.add(stroke((x, 0), (x, y1), arc(x + r, y1, r, r, 180, 58)))
    g.add(stroke((x - 110, XH - H), (x + 150, XH - H)))


@glyph("k", lsb=64, rsb=30)
def g_k(g):
    L, R = H, 400
    jy = 175
    g.add(stroke((L, 0), (L, AS)))
    arm = seg((R, XH), (L, jy), e0=40)
    j = (L + (R - L) * 0.36, jy + (XH - jy) * 0.36)
    leg = seg(j, (R + 25, 0), e1=40)
    g.add(clip(unary_union([arm, leg]), y0=0, y1=XH))


def vshape(L, R, top, bot=0):
    cx = (L + R) / 2
    a = seg((L, top), (cx, bot), e0=60, e1=60)
    b = seg((R, top), (cx, bot), e0=60, e1=60)
    return clip(unary_union([a, b]), y0=bot, y1=top)


@glyph("v", lsb=24)
def g_v(g):
    g.add(vshape(0, 460, XH))


@glyph("w", lsb=24)
def g_w(g):
    xs = [0, 175, 350, 525, 700]
    parts = [seg((xs[i], XH if i % 2 == 0 else 0), (xs[i + 1], 0 if i % 2 == 0 else XH), 60, 60)
             for i in range(4)]
    g.add(clip(unary_union(parts), y0=0, y1=XH))


@glyph("x", lsb=24)
def g_x(g):
    a = seg((0, XH), (440, 0), 60, 60)
    b = seg((0, 0), (440, XH), 60, 60)
    g.add(clip(unary_union([a, b]), y0=0, y1=XH))


@glyph("y", lsb=24)
def g_y(g):
    L, R = 0, 460
    cx = (L + R) / 2
    a = seg((L, XH), (cx, 0), e0=60)
    k = (R - cx) / XH
    b = seg((R, XH), (cx + k * DS, DS), e0=60, e1=60)
    g.add(clip(unary_union([a, b]), y0=DS, y1=XH))


@glyph("z", lsb=40)
def g_z(g):
    L, R = 0, 410
    g.add(stroke((L, XH - H), (R, XH - H)), stroke((L, H), (R + 10, H)))
    g.add(clip(seg((R - 18, XH - H), (L + 18, H), 60, 60), L - H, 0, R, XH))


@glyph("b", lsb=64, rsb=44)
def g_b(g):
    rx = 500 / 2 - H
    g.add(stroke((H, 0), (H, AS)), bowl(H + rx))


@glyph("d", lsb=44, rsb=64)
def g_d(g):
    rx = 500 / 2 - H
    R = 500 - H
    g.add(stroke((R, 0), (R, AS)), bowl(R - rx))


@glyph("p", lsb=64, rsb=44)
def g_p(g):
    rx = 500 / 2 - H
    g.add(stroke((H, DS), (H, XH)), bowl(H + rx))


@glyph("q", lsb=44, rsb=64)
def g_q(g):
    rx = 500 / 2 - H
    R = 500 - H
    g.add(stroke((R, DS), (R, XH)), bowl(R - rx))


@glyph("g", lsb=44, rsb=64)
def g_g(g):
    rx = 500 / 2 - H
    R = 500 - H
    rh, ryh = rx - 10, 150
    y0 = DS + H - OV / 2 + ryh
    g.add(bowl(R - rx))
    g.add(stroke((R, XH), (R, y0), arc(R - rh, y0, rh, ryh, 0, -148)))


@glyph("a", lsb=44, rsb=64)
def g_a(g):
    L, R = H, 440 - H
    rs = 150
    ys = XH + OV / 2 - H - rs
    cxs = (L + R) / 2 + 8
    g.add(stroke((R, 0), (R, ys), arc(cxs, ys, R - cxs, rs, 0, 152)))
    yb = 292
    cyb = (yb + H - OV / 2) / 2
    ryb = (yb - (H - OV / 2)) / 2
    cx1 = L + 135
    cx2 = R - 150
    g.add(stroke((R, yb), (cx1, yb), arc(cx1, cyb, 135, ryb, 90, 270),
                 (cx2, cyb - ryb), arc(cx2, cyb, R - cx2, ryb, 270, 360)))


# ------------------------------------------------------------- uppercase
@glyph("H", lsb=80)
def g_H(g):
    L, R = H, 560 - H
    g.add(stroke((L, 0), (L, CH)), stroke((R, 0), (R, CH)), stroke((L, 360), (R, 360)))


@glyph("I", lsb=80)
def g_I(g):
    g.add(stroke((H, 0), (H, CH)))


@glyph("L", lsb=80, rsb=30)
def g_L(g):
    g.add(stroke((H, 0), (H, CH)), stroke((H, H), (430, H)))


@glyph("E", lsb=80, rsb=50)
def g_E(g):
    L = H
    g.add(stroke((L, 0), (L, CH)), stroke((L, CH - H), (440, CH - H)),
          stroke((L, 362), (410, 362)), stroke((L, H), (450, H)))


@glyph("F", lsb=80, rsb=40)
def g_F(g):
    L = H
    g.add(stroke((L, 0), (L, CH)), stroke((L, CH - H), (430, CH - H)),
          stroke((L, 352), (400, 352)))


@glyph("T", lsb=24)
def g_T(g):
    ow = 540
    g.add(stroke((0, CH - H), (ow, CH - H)), stroke((ow / 2, 0), (ow / 2, CH)))


@glyph("O", lsb=48)
def g_O(g):
    ow, oh = 720, CH + 2 * OV
    g.add(ring(ow / 2, CH / 2, ow / 2 - H, oh / 2 - H))


@glyph("Q", lsb=48)
def g_Q(g):
    ow, oh = 720, CH + 2 * OV
    g.add(ring(ow / 2, CH / 2, ow / 2 - H, oh / 2 - H))
    g.add(stroke((ow / 2 + 120, 150), (ow - 10, -50)))


@glyph("C", lsb=48, rsb=40)
def g_C(g):
    ow, oh = 650, CH + 2 * OV
    g.add(stroke(arc(ow / 2, CH / 2, ow / 2 - H, oh / 2 - H, 42, 318)))


@glyph("G", lsb=48, rsb=60)
def g_G(g):
    ow, oh = 680, CH + 2 * OV
    cx, cy, rx, ry = ow / 2, CH / 2, ow / 2 - H, oh / 2 - H
    R = cx + rx
    g.add(stroke(arc(cx, cy, rx, ry, 42, 366)), stroke((cx + 150, 330), (R, 330)))


@glyph("D", lsb=80, rsb=48)
def g_D(g):
    L = H
    ry = CH / 2 - H
    rx = 300
    xa = L + 290
    g.add(stroke((L, 0), (L, CH)),
          stroke((L, CH - H), (xa - rx * 0.3, CH - H), arc(xa - rx * 0.3, CH / 2, rx, ry, 90, -90), (L, H)))


@glyph("B", lsb=80, rsb=50)
def g_B(g):
    L = H
    mid = 385
    ryu = (CH - H - mid) / 2
    ryl = (mid - H) / 2
    xa, xb = L + 245, L + 255
    g.add(stroke((L, 0), (L, CH)))
    g.add(stroke((L, CH - H), (xa, CH - H), arc(xa, mid + ryu, ryu * 1.02, ryu, 90, -90), (L, mid)))
    g.add(stroke((L, mid), (xb, mid), arc(xb, H + ryl, ryl * 1.02, ryl, 90, -90), (L, H)))


@glyph("P", lsb=80, rsb=40)
def g_P(g):
    L = H
    mid = 320
    ry = (CH - H - mid) / 2
    xa = L + 260
    g.add(stroke((L, 0), (L, CH)))
    g.add(stroke((L, CH - H), (xa, CH - H), arc(xa, mid + ry, ry * 1.02, ry, 90, -90), (L, mid)))


@glyph("R", lsb=80, rsb=40)
def g_R(g):
    L = H
    mid = 335
    ry = (CH - H - mid) / 2
    xa = L + 260
    g.add(stroke((L, 0), (L, CH)))
    g.add(stroke((L, CH - H), (xa, CH - H), arc(xa, mid + ry, ry * 1.02, ry, 90, -90), (L, mid)))
    g.add(clip(seg((xa - 20, mid), (xa + 215, 0), e1=50), y0=0))


@glyph("S", lsb=44)
def g_S(g):
    g.add(s_shape(CH, 540, 0.535))


@glyph("U", lsb=80)
def g_U(g):
    L, R = H, 590 - H
    ry = 250
    cx, rx = (L + R) / 2, (R - L) / 2
    yb = H - OV + ry
    g.add(stroke((L, CH), (L, yb), arc(cx, yb, rx, ry, 180, 360), (R, CH)))


@glyph("J", lsb=30, rsb=80)
def g_J(g):
    R, r = 400, 190
    y0 = H - OV + r
    g.add(stroke((R, CH), (R, y0), arc(R - r, y0, r, r * 1.05, 0, -165)))


@glyph("K", lsb=80, rsb=30)
def g_K(g):
    L, R = H, 540
    jy = 225
    g.add(stroke((L, 0), (L, CH)))
    arm = seg((R, CH), (L, jy), e0=50)
    t = 0.37
    j = (L + (R - L) * t, jy + (CH - jy) * t)
    leg = seg(j, (R + 20, 0), e1=50)
    g.add(clip(unary_union([arm, leg]), y0=0, y1=CH))


@glyph("A", lsb=20)
def g_A(g):
    ow = 640
    cx = ow / 2
    a = seg((0, 0), (cx, CH), 60, 60)
    b = seg((ow, 0), (cx, CH), 60, 60)
    yb = 215
    xl = cx * yb / CH
    g.add(clip(unary_union([a, b]), y0=0, y1=CH), stroke((xl, yb), (ow - xl, yb)))


@glyph("V", lsb=20)
def g_V(g):
    g.add(vshape(0, 620, CH))


@glyph("W", lsb=20)
def g_W(g):
    xs = [0, 230, 460, 690, 920]
    parts = [seg((xs[i], CH if i % 2 == 0 else 0), (xs[i + 1], 0 if i % 2 == 0 else CH), 60, 60)
             for i in range(4)]
    g.add(clip(unary_union(parts), y0=0, y1=CH))


@glyph("X", lsb=24)
def g_X(g):
    a = seg((0, CH), (590, 0), 60, 60)
    b = seg((0, 0), (590, CH), 60, 60)
    g.add(clip(unary_union([a, b]), y0=0, y1=CH))


@glyph("Y", lsb=20)
def g_Y(g):
    ow, jy = 600, 330
    cx = ow / 2
    a = seg((0, CH), (cx, jy), e0=60, e1=10)
    b = seg((ow, CH), (cx, jy), e0=60, e1=10)
    g.add(clip(unary_union([a, b]), y1=CH), stroke((cx, 0), (cx, jy + 10)))


@glyph("Z", lsb=44)
def g_Z(g):
    L, R = 0, 540
    g.add(stroke((L, CH - H), (R - 10, CH - H)), stroke((L, H), (R, H)))
    g.add(clip(seg((R - 22, CH - H), (L + 22, H), 60, 60), L - H, 0, R - 10, CH))


@glyph("M", lsb=80)
def g_M(g):
    L, R = H, 720 - H
    cx = (L + R) / 2
    g.add(stroke((L, 0), (L, CH)), stroke((R, 0), (R, CH)))
    d = unary_union([seg((L, CH), (cx, 0), 60, 60), seg((R, CH), (cx, 0), 60, 60)])
    g.add(clip(d, L - H, 0, R + H, CH))


@glyph("N", lsb=80)
def g_N(g):
    L, R = H, 590 - H
    g.add(stroke((L, 0), (L, CH)), stroke((R, 0), (R, CH)))
    g.add(clip(seg((L, CH), (R, 0), 60, 60), L - H, 0, R + H, CH))


# ------------------------------------------------------------------ figures
FIG = 580


def fig(ch, **kw):
    kw.setdefault("adv", FIG)
    return glyph(ch, **kw)


@fig("0")
def g_0(g):
    ow, oh = 490, CH + 2 * OV
    g.add(ring(ow / 2, CH / 2, ow / 2 - H, oh / 2 - H))


@fig("1")
def g_1(g):
    x = 230
    g.add(stroke((x, 0), (x, CH)))
    g.add(clip(seg((x + 10, CH - 10), (x - 175, CH - 175), e0=40), y1=CH))


@fig("2")
def g_2(g):
    L, R = 0, 440
    cx, rx, ry = 220, 220 - H, 200
    cy = CH + OV / 2 - H - ry
    g.add(stroke(arc(cx, cy, rx, ry, 158, -18), (L + 8, H), (R + 10, H), join="mitre"))


@fig("3")
def g_3(g):
    cx = 220
    mid = 395
    ryu = (CH + OV - H - mid) / 2
    ryl = (mid - (H - OV)) / 2
    g.add(stroke(arc(cx, mid + ryu, 185, ryu, 155, -90), arc(cx, mid - ryl, 205, ryl, 90, -155)))
    g.add(stroke((cx - 60, mid), (cx, mid)))


@fig("4")
def g_4(g):
    L, xs, yb = 0, 340, 215
    g.add(stroke((xs, 0), (xs, CH)))
    g.add(clip(stroke((xs, CH + 10), (L, yb), (L + 470, yb), join="mitre"), y0=0, y1=CH))


@fig("5")
def g_5(g):
    cx, cy, rx, ry = 225, 245, 215, 235 - OV
    t0 = 138
    a = arc(cx, cy, rx, ry, t0, -150)
    x0, y0 = a[0]
    g.add(stroke((cx + 195, CH - H), (x0, CH - H), a, join="mitre"))


@fig("6")
def g_6(g):
    cx, rx = 225, 215
    cy, ry = 240, 240 - OV - H + OV
    g.add(ring(cx, cy, rx, ry - OV))
    ry2 = CH + OV - H - cy
    g.add(stroke(arc(cx, cy, rx, ry2, 180, 58)))


@fig("9")
def g_9(g):
    g_6(g)
    g.parts = [affinity.rotate(unary_union(g.parts), 180, origin=(225 * SX, CH / 2))]


@fig("7")
def g_7(g):
    L, R = 0, 450
    g.add(clip(stroke((L, CH - H), (R, CH - H), (L + 150, -60), join="mitre"), y0=0, x1=R + 4))


@fig("8")
def g_8(g):
    cx, mid = 225, 395
    ryu = (CH + OV - H - mid) / 2
    ryl = (mid - (H - OV)) / 2
    g.add(ring(cx, mid + ryu, 185, ryu), ring(cx, mid - ryl, 210, ryl))


# -------------------------------------------------------------- punctuation


@glyph(".", lsb=70)
def g_period(g):
    g.add(dot(R_DOT, R_DOT))


@glyph(",", lsb=60)
def g_comma(g):
    g.add(dot(R_DOT, R_DOT), seg((R_DOT + 8, R_DOT), (R_DOT - 30, -130)))


@glyph(":", lsb=70)
def g_colon(g):
    g.add(dot(R_DOT, R_DOT), dot(R_DOT, XH - R_DOT))


@glyph(";", lsb=60)
def g_semicolon(g):
    g.add(dot(R_DOT, R_DOT), seg((R_DOT + 8, R_DOT), (R_DOT - 30, -130)), dot(R_DOT, XH - R_DOT))


@glyph("!", lsb=80)
def g_excl(g):
    g.add(stroke((R_DOT, 220), (R_DOT, CH)), dot(R_DOT, R_DOT))


@glyph("?", lsb=40)
def g_quest(g):
    cx, r = 190, 175
    cy = CH + OV - H - r
    g.add(stroke(arc(cx, cy, r, r, 160, -90), (cx, 230)), dot(cx, R_DOT))


@glyph("'", lsb=70)
def g_quote(g):
    g.add(stroke((H, CH), (H, CH - 210)))


@glyph('"', lsb=70)
def g_dquote(g):
    g.add(stroke((H, CH), (H, CH - 210)), stroke((H + 130, CH), (H + 130, CH - 210)))


@glyph("-", lsb=50)
def g_hyphen(g):
    g.add(stroke((0, 285), (230, 285)))


@glyph("–", lsb=40)
def g_endash(g):
    g.add(stroke((0, 285), (420, 285)))


@glyph("—", lsb=40)
def g_emdash(g):
    g.add(stroke((0, 285), (920, 285)))


@glyph("_", lsb=0)
def g_under(g):
    g.add(stroke((0, -120), (500, -120)))


@glyph("(", lsb=80, rsb=40)
def g_lparen(g):
    cy, ry = (AS + DS) / 2, 560
    g.add(clip(stroke(arc(330, cy, 300, ry, 120, 240, n=2)), y0=DS - 40, y1=AS + 40))


@glyph(")", lsb=40, rsb=80)
def g_rparen(g):
    cy, ry = (AS + DS) / 2, 560
    g.add(clip(stroke(arc(-130, cy, 300, ry, 60, -60, n=2)), y0=DS - 40, y1=AS + 40))


@glyph("[", lsb=90, rsb=40)
def g_lbrack(g):
    g.add(stroke((170, AS - H), (H, AS - H), (H, DS + H), (170, DS + H), join="mitre"))


@glyph("]", lsb=40, rsb=90)
def g_rbrack(g):
    g.add(stroke((0, AS - H), (170 - H, AS - H), (170 - H, DS + H), (0, DS + H), join="mitre"))


@glyph("/", lsb=10)
def g_slash(g):
    g.add(clip(seg((0, DS + 40), (330, AS), 50, 50), y0=DS + 40, y1=AS))


@glyph("\\", lsb=10)
def g_bslash(g):
    g.add(clip(seg((330, DS + 40), (0, AS), 50, 50), y0=DS + 40, y1=AS))


@glyph("+", lsb=60)
def g_plus(g):
    g.add(stroke((0, 300), (440, 300)), stroke((220, 80), (220, 520)))


@glyph("=", lsb=60)
def g_equal(g):
    g.add(stroke((0, 210), (440, 210)), stroke((0, 390), (440, 390)))


@glyph("<", lsb=70)
def g_less(g):
    g.add(stroke((420, 520), (0, 300), (420, 80), join="mitre"))


@glyph(">", lsb=70)
def g_greater(g):
    g.add(stroke((0, 520), (420, 300), (0, 80), join="mitre"))


@glyph("*", lsb=50)
def g_star(g):
    c = (170, CH - 170)
    for a in (90, 162, 234, 306, 18):
        t = math.radians(a)
        g.add(stroke(c, (c[0] + 170 * math.cos(t), c[1] + 170 * math.sin(t))))


@glyph("#", lsb=40)
def g_hash(g):
    g.add(stroke((0, 230), (520, 230)), stroke((20, 470), (540, 470)))
    g.add(clip(unary_union([seg((140, 0), (240, CH), 40, 40), seg((320, 0), (420, CH), 40, 40)]),
               y0=0, y1=CH))


@glyph("%", lsb=40)
def g_percent(g):
    g.add(ring(130, 560, 120, 140), ring(530, 150, 120, 140))
    g.add(clip(seg((40, 0), (620, CH), 40, 40), y0=0, y1=CH))


@glyph("&", lsb=44, rsb=30)
def g_amp(g):
    ucx, ucy, urx, ury = 215, CH + OV - H - 135, 118, 135
    lcx, lcy, lrx, lry = 225, 205 - OV / 2, 200, 205 - OV / 2 - H + OV / 2
    up = arc(ucx, ucy, urx, ury, 215, -48)
    lo = arc(lcx, lcy, lrx, lry, 128, 375)
    g.add(clip(stroke((600, -60), up, lo, (595, 330)), y0=0))


@glyph("@", lsb=50)
def g_at(g):
    cx, cy = 400, 250
    g.add(ring(cx, cy, 170, 195))
    g.add(stroke((cx + 170, 445), (cx + 170, 140), arc(cx + 270, 140, 100, 120, 180, 360),
                 arc(cx, cy, 370, 400, 0, 315)))


@glyph("$", lsb=44)
def g_dollar(g):
    g.add(s_shape(CH, 520, 0.535), stroke((260, -90), (260, CH + 90)))


@glyph("|", lsb=90)
def g_bar(g):
    g.add(stroke((H, DS), (H, AS)))


@glyph("^", lsb=60)
def g_caret(g):
    g.add(clip(unary_union([seg((0, 380), (170, CH), 0, 60), seg((340, 380), (170, CH), 0, 60)]), y1=CH))


@glyph("`", lsb=80)
def g_grave(g):
    g.add(seg((0, CH + 40), (100, CH - 90)))


@glyph("~", lsb=60)
def g_tilde(g):
    g.add(stroke(arc(110, 285, 110, 60, 180, 0, n=2), arc(330, 285, 110, 60, 180, 360, n=2)))


def brace(sign):
    cy, r, x0 = (AS + DS) / 2, 70, 0
    xa = x0 + sign * r
    xb = x0 + sign * 2 * r
    a0 = 90 if sign > 0 else 90
    pts = flat(arc(xb, AS - H - r, r, r, 90, 180) if sign > 0 else arc(xb, AS - H - r, r, r, 90, 0),
               arc(x0, cy + r, r, r, 0, -90) if sign > 0 else arc(x0, cy + r, r, r, 180, 270),
               arc(x0, cy - r, r, r, 90, 0) if sign > 0 else arc(x0, cy - r, r, r, 90, 180),
               arc(xb, DS + H + r, r, r, 180, 270) if sign > 0 else arc(xb, DS + H + r, r, r, 0, -90))
    return stroke(pts)


@glyph("{", lsb=50, rsb=40)
def g_lbrace(g):
    g.add(brace(1))


@glyph("}", lsb=40, rsb=50)
def g_rbrace(g):
    g.add(brace(-1))


@glyph("\u2018", lsb=70)
def g_lsquo(g):
    g.add(dot(R_DOT, CH - 140), seg((R_DOT - 8, CH - 140), (R_DOT + 30, CH + 10)))


@glyph("\u2019", lsb=70)
def g_rsquo(g):
    g.add(dot(R_DOT, CH - R_DOT), seg((R_DOT + 8, CH - R_DOT), (R_DOT - 30, CH - 180)))


@glyph("\u201C", lsb=70)
def g_ldquo(g):
    for x in (R_DOT, R_DOT + 120):
        g.add(dot(x, CH - 140), seg((x - 8, CH - 140), (x + 30, CH + 10)))


@glyph("\u201D", lsb=70)
def g_rdquo(g):
    for x in (R_DOT, R_DOT + 120):
        g.add(dot(x, CH - R_DOT), seg((x + 8, CH - R_DOT), (x - 30, CH - 180)))


@glyph("\u2026", lsb=70)
def g_ellipsis(g):
    for i in range(3):
        g.add(dot(R_DOT + i * 230, R_DOT))


@glyph("\u2022", lsb=70)
def g_bullet(g):
    g.add(dot(90, 300, 90))


@glyph("\u00B7", lsb=70)
def g_middot(g):
    g.add(dot(R_DOT, XH / 2 + 20))


@glyph("\u00D7", lsb=70)
def g_times(g):
    g.add(stroke((0, 110), (360, 470)), stroke((0, 470), (360, 110)))


@glyph("\u00B0", lsb=60)
def g_degree(g):
    g.add(ring(110, CH - 110, 95, 95))


# ------------------------------------------------------------------- build
def to_glyph(geom):
    pen = TTGlyphPen(None)
    polys = getattr(geom, "geoms", [geom])
    for p in polys:
        if p.is_empty or p.geom_type != "Polygon":
            continue
        p = orient(p.simplify(0.35), sign=-1.0)
        for ring_ in [p.exterior, *p.interiors]:
            pts = [(round(x), round(y)) for x, y in ring_.coords[:-1]]
            clean = []
            for q in pts:
                if not clean or q != clean[-1]:
                    clean.append(q)
            if len(clean) > 1 and clean[0] == clean[-1]:
                clean.pop()
            if len(clean) < 3:
                continue
            pen.moveTo(clean[0])
            for q in clean[1:]:
                pen.lineTo(q)
            pen.closePath()
    return pen.glyph()


def gname(ch):
    special = {" ": "space", " ": "uni00A0"}
    if ch in special:
        return special[ch]
    if ch.isalnum() and ch.isascii():
        return ch if not ch.isdigit() else ["zero", "one", "two", "three", "four",
                                              "five", "six", "seven", "eight", "nine"][int(ch)]
    return "uni%04X" % ord(ch)


KERN = """
@T = [T];
@VW = [V W];
@Y = [Y];
@round_lc = [a c d e g o q s];
@diag_lc = [v w y];
@punct = [uni002E uni002C uni2026];
@quote = [uni0027 uni0022 uni2019 uni201D];
@open_uc = [A];
@FP = [F P];
@L = [L];
@r = [r];
feature kern {
  pos @T @round_lc -70;  pos @T [u r z m n p x] -50;  pos @T @diag_lc -40;
  pos @T @punct -80;  pos @T @open_uc -50;  pos @open_uc @T -50;
  pos @VW @round_lc -40;  pos @VW @punct -70;  pos @VW @open_uc -35;  pos @open_uc @VW -35;
  pos @Y @round_lc -60;  pos @Y @punct -80;  pos @Y @open_uc -50;  pos @open_uc @Y -50;
  pos @open_uc @diag_lc -15;  pos @open_uc @quote -50;  pos @quote @open_uc -50;
  pos @L @T -70;  pos @L @VW -50;  pos @L @Y -70;  pos @L @quote -70;  pos @L @diag_lc -20;
  pos @FP @punct -90;  pos @FP @open_uc -30;  pos @FP @round_lc -15;
  pos @r @punct -50;  pos @diag_lc @punct -45;
  pos [f] @quote 30;  pos @quote @round_lc -25;
} kern;
"""


def build_weight(style, weight, wclass):
    from fontTools.feaLib.builder import addOpenTypeFeaturesFromString

    set_weight(weight)
    order = [".notdef", "space", "uni00A0"]
    cmap = {0x20: "space", 0xA0: "uni00A0"}
    glyphs, metrics = {}, {}

    pen = TTGlyphPen(None)
    for r in ((50, 0, 450, CH), (100, 50, 400, CH - 50)):
        x0, y0, x1, y1 = r
        pts = [(x0, y0), (x0, y1), (x1, y1), (x1, y0)]
        if r[0] == 100:
            pts.reverse()
        pen.moveTo(pts[0])
        for q in pts[1:]:
            pen.lineTo(q)
        pen.closePath()
    glyphs[".notdef"] = pen.glyph()
    metrics[".notdef"] = (500, 50)
    empty = TTGlyphPen(None).glyph()
    for n in ("space", "uni00A0"):
        glyphs[n] = empty
        metrics[n] = (round(260 * SB), 0)

    for ch, (fn, kw) in GLYPHS.items():
        lsb = kw.get("lsb", 60)
        rsb = kw.get("rsb", lsb)
        adv = kw.get("adv")
        g = Glyph(lsb=lsb * SB, rsb=rsb * SB, adv=adv and round(adv * SX))
        fn(g)
        geom = g.geometry()
        minx, _, maxx, _ = geom.bounds
        if g.adv:  # fixed width (figures): centre
            adv = g.adv
            dx = (adv - (maxx - minx)) / 2 - minx
        else:
            dx = g.lsb - minx
            adv = round(maxx - minx + g.lsb + g.rsb)
        geom = affinity.translate(geom, xoff=round(dx))
        name = gname(ch)
        glyphs[name] = to_glyph(geom)
        metrics[name] = (adv, round(geom.bounds[0]))
        order.append(name)
        cmap[ord(ch)] = name

    bold = style == "Bold"
    ribbi = style in ("Regular", "Bold")
    ps = f"{FAMILY.replace(' ', '')}-{style}"
    names = {
        "familyName": FAMILY if ribbi else f"{FAMILY} {style}",
        "styleName": style if ribbi else "Regular",
        "uniqueFontIdentifier": f"{ps};{VERSION}",
        "fullName": f"{FAMILY} {style}",
        "psName": ps,
        "version": f"Version {VERSION}",
    }
    if not ribbi:
        names["typographicFamily"] = FAMILY
        names["typographicSubfamily"] = style

    fb = FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap(cmap)
    fb.setupGlyf(glyphs)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=950, descent=-250, lineGap=0)
    fb.setupOS2(
        sTypoAscender=800, sTypoDescender=-220, sTypoLineGap=180,
        usWinAscent=980, usWinDescent=280, sxHeight=XH, sCapHeight=CH,
        version=4, usWeightClass=wclass,
        fsSelection=(0x20 if bold else 0x40) | 0x80, achVendID="NONE",
    )
    fb.setupNameTable(names)
    fb.setupPost()
    fb.setupHead(unitsPerEm=UPM, macStyle=1 if bold else 0)
    font = fb.font
    font["head"].fontRevision = float(VERSION)
    addOpenTypeFeaturesFromString(font, KERN)

    ttf = os.path.join(OUT, f"{ps}.ttf")
    font.save(ttf)
    try:  # hinting sharpens small sizes on Windows
        from ttfautohint import ttfautohint
        ttfautohint(in_file=ttf, out_file=ttf, hinting_limit=72)
    except ImportError:
        print("  (ttfautohint-py not installed: font left unhinted)")
    from fontTools.ttLib import TTFont
    web = TTFont(ttf)
    web.flavor = "woff2"
    web.save(os.path.join(OUT, f"{ps}.woff2"))
    print("wrote", ttf, "glyphs:", len(order))
    return ttf


def build():
    return [build_weight(*w) for w in WEIGHTS]


if __name__ == "__main__":
    build()
