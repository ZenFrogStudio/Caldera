# Caldera Sans Light

An original light, monoline sans-serif: round geometric bowls, a double-story `a`,
single-story `g`, an angle-cut `t` and a straight-tailed `y`.

Files:
- `CalderaSans-Light.ttf`: desktop and app use
- `CalderaSans-Light.woff2`: web use
- `specimen.png`: preview
- `src/build_font.py`: generator; every glyph is defined as centre-line strokes

It covers printable ASCII plus curly quotes, en and em dashes, ellipsis, bullet and degree sign.

## Rebuild

```bash
pip install fonttools shapely brotli pillow
python fonts/src/build_font.py
python fonts/src/specimen.py fonts/CalderaSans-Light.ttf fonts/specimen.png
```

Tweak `W` (weight), `SX` (width), `XH`/`CH` (x/cap height) or `SE` (roundness) at the top of the script.

## Web use

```css
@font-face {
  font-family: "Caldera Sans";
  src: url("fonts/CalderaSans-Light.woff2") format("woff2");
  font-weight: 300;
}
```
