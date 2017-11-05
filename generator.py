# encoding:utf-8
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# d1 = Image.open('1.png')
# d2 = Image.open('2.png')
i1 = Image.new("RGB", (500, 200), (120, 150, 200))
# i1.show()
px = i1.getdata()

px2 = list(px)
ppp = np.array(px2)
print( i1.size[0], i1.size[1], i1)
mtp = ppp.reshape(i1.size[1], i1.size[0], 3)
mtpr = np.random.rand(i1.size[1] * i1.size[0]
                      ).reshape(i1.size[1], i1.size[0])

for x in range(0, i1.size[1]):
    for y in range(0, i1.size[0]):
        mtpr[x][y] = mtp[x][y][0]
        # print( y + (i1.size[0]) * x,)
print
tt = 0
for x1 in range(0, i1.size[1]):
    for y1 in range(0, i1.size[0]):
        mtpr[x1, y1] *= tt / 25000.0
        tt += 1
# print( tt)

for x in range(0, i1.size[1]):
    for y in range(0, i1.size[0]):
        rr = int(mtpr[x][y])
        val = (y + x) / 350.0
        val *= np.pi
        # print( "%2.2f" % val,)
        px2[y + (i1.size[0]) * x] = (int(255 * (np.sin(val * 0.5) * 0.3 + 0.5)),
                                     int(255 * (np.sin(val * 2) * 0.4 + 0.6)), int(255 * (np.sin(val * 0.5) * 0.3 + 0.7)))
        # print( y + (i1.size[0]) * x,)
i1.putdata(px2)


i2 = Image.new("RGB", (500, 200), (0, 0, 0))
draw = ImageDraw.Draw(i2)
font = ImageFont.truetype(
    '/Library/Fonts/ヒラギノ角ゴシック W7.ttc', 125, encoding='unic')
draw.text((37.5, 37.5), u'超級悪鬼',
          font=font, fill=(255, 255, 255))

p1 = i1.getdata()
p1 = list(p1)
p2 = i2.getdata()
p2 = list(p2)
# print( p1)
d = 50
for yy in range(1, d + 1):

    # i3 = i2
    p3 = i2.getdata()
    p3 = list(p3)
    for x in range(0, 500 * 200):
        if p3[x][0] == 255:
            val = np.sin(np.pi * (yy / (float(d)))) * 0.5 + 0.5
            xx = (int(p1[x - yy * 10][0] * val),
                  int(p1[x - yy * 10][1] * val),
                  int(p1[x - yy * 10][2] * val))
            p3[x] = xx
        else:
            xx = (int(p1[x][0] * val+1),
                  int(p1[x][1] * val+1),
                  int(p1[x][2] * val+1))

            p3[x] = xx
    i3 = Image.new("RGB", (500, 200), (0, 0, 0))
    i3.putdata(p3)
    # i2.show()
    st = str((yy+25)%50)
    i3.save(st.zfill(3) + ".png")

# i1.save('aaas.png')
