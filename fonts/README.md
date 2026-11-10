# Caldera Sans

A clean, highly readable sans-serif for interfaces and body text, in **Light**, **Regular** and **Bold**.

Built for legibility:
- Tall x-height, so letters stay clear at small sizes
- Open shapes in `c`, `e`, `s` and `a`
- Look-alike characters are easy to tell apart: `I l 1 |` (the `l` has a tail) and `O 0`
- Horizontal strokes are slightly thinner than vertical ones, for an even texture
- Kerned and autohinted for crisp rendering on Windows

Covers printable ASCII plus curly quotes, dashes, ellipsis, bullet, middle dot, `×` and `°`.

## Files

| Weight  | Desktop / app             | Web                         |
|---------|---------------------------|-----------------------------|
| Light   | `CalderaSans-Light.ttf`   | `CalderaSans-Light.woff2`   |
| Regular | `CalderaSans-Regular.ttf` | `CalderaSans-Regular.woff2` |
| Bold    | `CalderaSans-Bold.ttf`    | `CalderaSans-Bold.woff2`    |

`specimen.png` is a preview. `src/build_font.py` generates every weight; each glyph is defined as centre-line strokes.

## Rebuild

```bash
pip install fonttools shapely brotli ttfautohint-py pillow
python fonts/src/build_font.py
python fonts/src/specimen.py fonts fonts/specimen.png
```

Change `WEIGHTS`, `XH`/`CH` (x/cap height), `CONTRAST` or `SE` (roundness) at the top of the script to adjust the design.

## Web use

```css
@font-face { font-family: "Caldera Sans"; src: url("fonts/CalderaSans-Light.woff2") format("woff2"); font-weight: 300; }
@font-face { font-family: "Caldera Sans"; src: url("fonts/CalderaSans-Regular.woff2") format("woff2"); font-weight: 400; }
@font-face { font-family: "Caldera Sans"; src: url("fonts/CalderaSans-Bold.woff2") format("woff2"); font-weight: 700; }

body { font-family: "Caldera Sans", system-ui, sans-serif; }
```
