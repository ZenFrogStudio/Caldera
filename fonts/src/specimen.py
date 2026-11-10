"""Render a specimen of the Caldera Sans family: python specimen.py <fonts_dir> <out.png>"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

d_in, out = sys.argv[1], sys.argv[2]
F = lambda style, size: ImageFont.truetype(os.path.join(d_in, f"CalderaSans-{style}.ttf"), size)
INK, MUTED, BG = (24, 24, 27), (113, 113, 122), (250, 250, 249)

para = ("Good type disappears. When letters are open, evenly spaced and clearly "
        "distinct, the reader stops noticing them and simply reads.")
img = Image.new("RGB", (1600, 1180), BG)
d = ImageDraw.Draw(img)
y = 40
d.text((60, y), "Caldera Sans", font=F("Bold", 96), fill=INK); y += 130
for style in ("Light", "Regular", "Bold"):
    d.text((60, y), f"{style}  —  The quick brown fox jumps over the lazy dog", font=F(style, 46), fill=INK)
    y += 70
y += 20
d.text((60, y), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", font=F("Regular", 56), fill=INK); y += 76
d.text((60, y), "abcdefghijklmnopqrstuvwxyz", font=F("Regular", 56), fill=INK); y += 76
d.text((60, y), "0123456789  .,:;!?'\"-()[]{}/&@$%#*+=<>", font=F("Regular", 56), fill=INK); y += 100
d.text((60, y), "Look-alikes stay distinct:   Il1|   O0   rn m   cl d", font=F("Regular", 44), fill=INK); y += 90
for size in (13, 16, 20, 26):
    d.text((60, y), f"{size}px", font=F("Regular", 14), fill=MUTED)
    d.text((130, y), para, font=F("Regular", size), fill=INK)
    y += int(size * 1.9) + 10
y += 10
for size in (16, 26):
    d.text((60, y), "Bold", font=F("Regular", 14), fill=MUTED)
    d.text((130, y), "Team standup · Thursday 10:30 – 11:00 · Room 4B", font=F("Bold", size), fill=INK)
    y += int(size * 1.9) + 10
img = img.crop((0, 0, 1600, y + 30))
img.save(out)
