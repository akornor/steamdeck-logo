# Copied from https://github.com/mitchgu/scorpics/blob/master/make_collage.py
from pathlib import Path
from PIL import Image


SIZE = (3,4)
N = SIZE[0]*SIZE[1] 
IMG_SIZE = (550,550)
PAD = 50
COLLAGE_SIZE = (SIZE[0]*(IMG_SIZE[0]+PAD)+PAD, SIZE[1]*(IMG_SIZE[1]+PAD)+PAD)

collage = Image.new("RGB", COLLAGE_SIZE, color=(0x0A, 0x0A, 0x0A))

imgs = sorted(Path("img").glob("*.jpg"))
assert len(imgs) >= N
for i in range(N):
    col = i % SIZE[0]
    row = i // SIZE[0]
    upper_left = ((IMG_SIZE[0] + PAD) * col + PAD, (IMG_SIZE[0] + PAD) * row + PAD)
    img = Image.open(imgs[i])
    collage.paste(img, upper_left)

collage.save(Path("collage.jpg"))