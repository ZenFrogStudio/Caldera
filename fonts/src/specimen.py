import sys
from PIL import Image, ImageDraw, ImageFont
ttf, out = sys.argv[1], sys.argv[2]
lines = [(83, "In other words, if a person only ever"), (83, "sees a few typefaces, and does not see"),
         (83, "anything else, he will only ever think"), (83, "they are beautiful."),
         (60, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"), (60, "abcdefghijklmnopqrstuvwxyz"),
         (60, "0123456789 .,:;!?'\"-()[]/&@$%#*+=<>")]
img = Image.new("RGB", (1500, 900), "black"); d = ImageDraw.Draw(img); y = 20
for s, t in lines:
    f = ImageFont.truetype(ttf, s); d.text((30, y), t, font=f, fill="white"); y += int(s * 1.2)
img.save(out)
