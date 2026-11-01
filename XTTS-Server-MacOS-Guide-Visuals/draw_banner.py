#!/usr/bin/env python3
"""XTTS wordmark banner: post road station at first light, name painted on the gate board in Arya."""
import math, random
from PIL import Image, ImageDraw, ImageFont
random.seed(23)
HERE=__file__.rsplit('/',1)[0]
W,H=1200,420
PORC=(247,244,235); DBLUE=(28,52,102); CIN=(178,44,32); PINE=(38,92,66)
img=Image.new('RGB',(W,H),(206,220,236)); d=ImageDraw.Draw(img,'RGBA')
for y in range(0,170):
    t=y/170; d.line([(0,y),(W,y)],fill=(int(206-24*t),int(220-22*t),int(236-52*t)))
d.polygon([(0,168),(300,128),(620,158),(900,132),(1200,162),(1200,240),(0,240)],fill=(96,120,152))
d.rectangle([0,228,W,H],fill=(178,150,110))
for _ in range(1800):
    x,y=random.uniform(0,W),random.uniform(228,H); d.point((x,y),fill=random.choice([(160,130,90),(190,162,120)]))
# road in from lower left to gate
d.polygon([(0,420),(0,330),(330,268),(520,262),(430,420)],fill=(158,126,88))
for t in (0.3,0.6):
    pts=[((1-u)*(30+t*70)+u*(380+t*60),(1-u)*412+u*272) for u in [i/16 for i in range(17)]]
    d.line(pts,fill=(122,96,66),width=4)
# station building
bx,by=470,196
d.rectangle([bx,by+36,bx+440,by+104],fill=(232,224,204))
d.polygon([(bx-16,by+40),(bx+456,by+40),(bx+408,by),(bx+32,by)],fill=PINE)
for i in range(13):
    x=bx+8+i*33; d.line([(x,by+38),(x+14,by+3)],fill=(30,76,54),width=2)
d.line([(bx+32,by+2),(bx+408,by+2)],fill=(240,196,120),width=3)
d.rectangle([bx+54,by+56,bx+96,by+104],fill=(92,66,44))
# gate with name board
gx=270
f=ImageFont.truetype(HERE+'/fonts/Arya.ttf',30)
t='XTTS-Server-MacOS-Guide'
bb=d.textbbox((0,0),t,font=f); tw=bb[2]-bb[0]
bw=tw+36
d.rectangle([gx,150,gx+16,300],fill=(84,58,36)); d.rectangle([gx+bw-16,150,gx+bw,300],fill=(84,58,36))
d.rectangle([gx-8,138,gx+bw+8,186],fill=DBLUE)
d.rectangle([gx-8,138,gx+bw+8,186],outline=(16,34,72),width=3)
d.text((gx+bw/2-tw/2-bb[0],150-bb[1]),t,font=f,fill=(255,255,255))
# clerk at standing desk holding tablet up to light
dx,dy=600,296
d.polygon([(dx,dy),(dx+84,dy),(dx+76,dy+9),(dx+8,dy+9)],fill=(110,80,50))
d.line([(dx+12,dy+9),(dx+9,dy+48)],fill=(110,80,50),width=5); d.line([(dx+72,dy+9),(dx+75,dy+48)],fill=(110,80,50),width=5)
for i in range(5):
    x=dx+52+i*7; d.rectangle([x,dy-44,x+5,dy-18],fill=(206,180,120),outline=(150,124,78))
d.ellipse([dx+30,dy-34,dx+44,dy-20],fill=(70,52,38))  # clerk head
d.polygon([(dx+24,dy-20),(dx+50,dy-20),(dx+54,dy+8),(dx+20,dy+8)],fill=DBLUE)  # clerk body
d.line([(dx+48,dy-14),(dx+58,dy-34)],fill=DBLUE,width=5)  # arm up to tablet
# horses waiting, trough, hitching post
def horse(x,y,s,c=(102,78,56)):
    for i,lx in enumerate([x+14*s,x+30*s,x+62*s,x+78*s]):
        d.line([(lx,y+26*s),(lx,y+72*s)],fill=c,width=max(3,int(6*s)))
    d.ellipse([x,y,x+92*s,y+36*s],fill=c)
    d.polygon([(x+66*s,y+2*s),(x+94*s,y+2*s),(x+102*s,y+10*s),(x+78*s,y+18*s)],fill=c)
    d.polygon([(x+90*s,y),(x+116*s,y+8*s),(x+114*s,y+18*s),(x+92*s,y+18*s)],fill=c)
    d.line([(x+8*s,y+6*s),(x-10*s,y+30*s)],fill=c,width=max(3,int(5*s)))
horse(742,300,0.9); horse(838,308,0.84)
tx,ty=724,368
d.polygon([(tx,ty),(tx+120,ty),(tx+108,ty+20),(tx+12,ty+20)],fill=(104,76,48))
d.ellipse([tx+4,ty-4,tx+116,ty+6],fill=(168,196,220))
# departing rider through far gate at right, dust behind hooves
rx,ry=1020,286
horse(rx,ry,0.95,(88,66,46))
d.ellipse([rx+32,ry-40,rx+46,ry-26],fill=(70,52,38))
d.polygon([(rx+26,ry-28),(rx+52,ry-28),(rx+54,ry-4),(rx+24,ry-4)],fill=CIN)
d.line([(rx+46,ry-6),(rx+58,ry+22)],fill=(52,40,28),width=6)
d.line([(rx+30,ry-6),(rx+24,ry+20)],fill=(52,40,28),width=6)
d.rectangle([rx+54,ry-14,rx+70,ry+4],fill=(120,84,40))  # sealed dispatch pouch
for i in range(14):
    x,y=rx-8-i*7,ry+66+random.uniform(-4,8); r=3+i*0.8
    d.ellipse([x-r,y-r*0.5,x+r,y+r*0.5],fill=(196,168,128,150))
d.rectangle([1150,196,1164,300],fill=(84,58,36))
# kitchen bench with steaming bowls
kx,ky=520,352
d.rectangle([kx,ky,kx+110,ky+9],fill=(110,80,50))
for i in range(3):
    d.ellipse([kx+10+i*34,ky-11,kx+36+i*34,ky],fill=(222,216,200),outline=(150,140,120))
    for j in range(5):
        t=j/5; d.ellipse([kx+20+i*34+math.sin(t*3)*3,ky-16-t*22,kx+24+i*34,ky-13-t*22],fill=(245,244,238,130))
# long shadows toward building
for (x,y,w) in [(330,296,220),(724,388,120),(600,344,80)]:
    d.polygon([(x,y),(x+w,y+3),(x+w+40,y+12),(x,y+9)],fill=(120,94,62,100))
from PIL import ImageFilter
img=img.filter(ImageFilter.GaussianBlur(0.5))
img.save(HERE+'/banner.png')
print('saved')
