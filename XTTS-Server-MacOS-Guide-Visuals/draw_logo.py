#!/usr/bin/env python3
"""XTTS logo: bound bamboo post tablet, cinnabar seal dab, cropped pine tile gate roof, Arya wordmark."""
from PIL import Image, ImageDraw, ImageFont
HERE=__file__.rsplit('/',1)[0]
W,H=760,560
img=Image.new('RGB',(W,H),(247,244,235)); d=ImageDraw.Draw(img)
PINE=(38,92,66); CIN=(178,44,32); DBLUE=(28,52,102)
# cropped gate roof behind, low
d.polygon([(90,300),(670,300),(590,238),(170,238)],fill=PINE)
for i in range(11):
    x=180+i*42; d.line([(x,296),(x+22,242)],fill=(30,76,54),width=3)
# bamboo tablet: nine strips, top strip longer
tx,ty,sw,sh=190,90,42,300
for i in range(9):
    x=tx+i*sw; top=ty-22 if i==0 else ty
    d.rectangle([x,top,x+sw-5,ty+sh],fill=(208,182,122),outline=(148,122,74),width=2)
    d.line([(x+8,top+16),(x+8,ty+sh-16)],fill=(188,158,100),width=2)
# two dark cords across the backs (drawn over front, lashing)
for cy in (ty+72,ty+216):
    d.rectangle([tx-12,cy,tx+9*sw+2,cy+13],fill=(52,40,28))
    for i in range(9):
        x=tx+i*sw; d.rectangle([x,cy,x+sw-5,cy+13],fill=(64,50,34))
# cinnabar seal dab, lower right of front strip
import random; random.seed(7)
cx,cy=tx+8*sw+14,ty+sh-44
for _ in range(60):
    import math; a=random.uniform(0,6.28); r=random.uniform(0,17)
    d.ellipse([cx+math.cos(a)*r-3,cy+math.sin(a)*r-3,cx+math.cos(a)*r+3,cy+math.sin(a)*r+3],fill=CIN)
d.ellipse([cx-15,cy-15,cx+15,cy+15],outline=CIN,width=2)
# wordmark in Arya
f=ImageFont.truetype(HERE+'/fonts/Arya.ttf',44)
t='XTTS-Server-MacOS-Guide'
bb=d.textbbox((0,0),t,font=f); tw=bb[2]-bb[0]
d.text(((W-tw)/2-bb[0],448),t,font=f,fill=DBLUE)
img.save(HERE+'/logo.png')
img.resize((64,64)).save(HERE+'/scratch/logo64-ship.png')
print('saved')
