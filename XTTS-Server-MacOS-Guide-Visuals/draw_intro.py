#!/usr/bin/env python3
"""XTTS intro banner: Han post road relay station yard at dawn, no text anywhere."""
import math, random
from PIL import Image, ImageDraw
random.seed(41)
W,H=1200,520
PORC=(247,244,235); DBLUE=(28,52,102); CIN=(178,44,32); PINE=(38,92,66); EARTH=(146,116,82); EARTHD=(110,84,58)
img=Image.new('RGB',(W,H),(198,214,232)); d=ImageDraw.Draw(img,'RGBA')
# sky gradient dawn: pale top to warm at ridge
for y in range(0,240):
    t=y/240; d.line([(0,y),(W,y)],fill=(int(198-30*t),int(214-26*t),int(232-60*t)))
# ridge
d.polygon([(0,235),(180,190),(360,215),(560,168),(760,205),(950,178),(1200,215),(1200,300),(0,300)],fill=(92,116,150))
d.polygon([(0,268),(240,238),(520,262),(820,240),(1200,266),(1200,330),(0,330)],fill=(70,96,124))
# warm light catching ridge top
d.line([(560,168),(760,205)],fill=(240,196,120),width=4); d.line([(180,190),(360,215)],fill=(238,190,110),width=3)
# watch platform on ridge (empty)
px,py=905,150
d.rectangle([px,py,px+54,py+16],fill=(60,50,40)); d.polygon([(px-6,py),(px+60,py),(px+46,py-14),(px+8,py-14)],fill=PINE)
for lx in (px+4,px+46): d.line([(lx,py+16),(lx,py+42)],fill=(60,50,40),width=4)
# pine trees along far road
def pine(x,y,s):
    d.line([(x,y),(x,y-26*s)],fill=(74,58,40),width=max(2,int(3*s)))
    for i in range(3):
        wdt=(26-i*6)*s; yy=y-(14+i*11)*s
        d.polygon([(x-wdt,yy),(x+wdt,yy),(x,yy-16*s)],fill=(44,92,64))
for (x,y,s) in [(120,268,1.0),(210,258,0.8),(1010,252,0.9),(1090,262,1.1),(700,246,0.7),(640,252,0.85)]:
    pine(x,y,s)
# far road climbing in a bend
d.polygon([(700,300),(760,272),(880,252),(960,238),(940,228),(850,238),(740,262),(668,292)],fill=(168,140,102))
# ground: yard earth
d.rectangle([0,300,W,H],fill=(178,150,110))
for _ in range(2600):
    x,y=random.uniform(0,W),random.uniform(300,H); c=random.choice([(160,130,90),(190,162,120),(146,116,82)])
    d.point((x,y),fill=c)
# foreground road from lower left with ruts, stones, broken tile, puddle
d.polygon([(0,520),(0,392),(300,330),(520,318),(430,520)],fill=(158,126,88))
for t in (0.32,0.62):
    pts=[]
    for i in range(21):
        u=i/20; x=(1-u)*10+u*430 + t*((1-u)*0+u*90- (1-u)*0) ; x=(1-u)*(20+t*60)+u*(360+t*70); y=(1-u)*512+u*330
        pts.append((x,y))
    d.line(pts,fill=(122,96,66),width=4)
for _ in range(46):
    x,y=random.uniform(10,430),random.uniform(360,510); r=random.uniform(2,6)
    d.ellipse([x-r,y-r*0.6,x+r,y+r*0.6],fill=(128,112,92))
d.polygon([(238,452),(268,446),(276,462),(246,468)],fill=(150,70,52))  # broken roof tile
d.ellipse([120,452,268,492],fill=(196,216,234))  # puddle holding pale sky
d.ellipse([120,452,268,492],outline=(110,90,64),width=2)
# hoofprints crossing diagonally
for i in range(7):
    x,y=90+i*52,420-i*13; d.arc([x,y,x+13,y+9],200,340,fill=(96,74,50),width=3)
# yard buildings: long low station with pine green tiled roof
bx,by=430,268
d.rectangle([bx,by+38,bx+430,by+108],fill=(232,224,204))
d.polygon([(bx-16,by+42),(bx+446,by+42),(bx+400,by),(bx+30,by)],fill=PINE)
for i in range(13):
    x=bx+6+i*33; d.line([(x,by+40),(x+14,by+3)],fill=(30,76,54),width=2)
d.rectangle([bx+52,by+58,bx+96,by+108],fill=(92,66,44))  # door
d.rectangle([bx+300,by+56,bx+352,by+92],fill=(206,196,168),outline=(92,66,44),width=2)  # window
# warm dawn light on roof tiles
d.line([(bx+30,by+2),(bx+400,by+2)],fill=(240,196,120),width=3)
# gate open with bar lifted, foreground left of building
gx=352
d.rectangle([gx,238,gx+14,356],fill=(84,58,36)); d.rectangle([gx+118,238,gx+132,356],fill=(84,58,36))
d.rectangle([gx-4,232,gx+136,246],fill=DBLUE)  # gate board, blank in intro (no text)
d.line([(gx+10,300),(gx+118,262)],fill=(84,58,36),width=6)  # lifted bar diagonal
# standing desk under eaves with bamboo tablet weighted by stone, ink bowl, brush
dx,dy=520,368
d.polygon([(dx,dy),(dx+86,dy),(dx+78,dy+10),(dx+8,dy+10)],fill=(110,80,50))
d.line([(dx+12,dy+10),(dx+8,dy+52)],fill=(110,80,50),width=5); d.line([(dx+74,dy+10),(dx+78,dy+52)],fill=(110,80,50),width=5)
for i in range(6):
    x=dx+16+i*8; d.rectangle([x,dy-16,x+6,dy-2],fill=(206,180,120),outline=(150,124,78))
d.ellipse([dx+52,dy-22,dx+68,dy-12],fill=(96,90,84))  # smooth stone weight
d.ellipse([dx+96,dy-8,dx+116,dy+2],fill=(30,30,34))  # ink bowl
d.line([(dx+92,dy+6),(dx+118,dy+2)],fill=(60,44,28),width=3)  # brush on saucer
d.ellipse([dx+88,dy+2,dx+122,dy+10],outline=(120,100,70))
# trough full and still + hitching post
tx,ty=742,428
d.polygon([(tx,ty),(tx+130,ty),(tx+118,ty+22),(tx+12,ty+22)],fill=(104,76,48))
d.ellipse([tx+4,ty-4,tx+126,ty+6],fill=(168,196,220))
d.line([(tx-26,ty-58),(tx-26,ty+20)],fill=(84,58,36),width=7); d.line([(tx-26,ty-52),(tx+120,ty-52)],fill=(84,58,36),width=4)
# horses: two dozing at post, one stamping by stable door
def horse(x,y,s,head_down=1,stamp=False):
    c=(102,78,56)
    # legs first
    for i,lx in enumerate([x+14*s,x+30*s,x+62*s,x+78*s]):
        ly=y+74*s if not (stamp and i==3) else y+52*s
        d.line([(lx,y+26*s),(lx,ly)],fill=c,width=max(3,int(6*s)))
        d.line([(lx,ly),(lx+9*s,ly)],fill=(80,60,40),width=max(2,int(4*s)))
    # body
    d.ellipse([x,y,x+92*s,y+36*s],fill=c)
    # neck and head, lowered for dozing horses
    drop=16*s*head_down
    d.polygon([(x+66*s,y+2*s),(x+94*s,y-14*s+drop),(x+102*s,y-6*s+drop),(x+78*s,y+18*s)],fill=c)
    d.polygon([(x+90*s,y-16*s+drop),(x+116*s,y-8*s+drop),(x+114*s,y+2*s+drop),(x+92*s,y+2*s+drop)],fill=c)
    d.polygon([(x+92*s,y-16*s+drop),(x+96*s,y-24*s+drop),(x+100*s,y-15*s+drop)],fill=c)  # ear
    d.line([(x+8*s,y+6*s),(x-10*s,y+30*s)],fill=c,width=max(3,int(5*s)))  # tail
horse(700,374,1.02,1); horse(818,382,0.95,1)
d.rectangle([972,306,1096,420],fill=(216,204,178))  # stable
d.polygon([(962,308),(1106,308),(1072,272),(996,272)],fill=PINE)
d.rectangle([1018,344,1064,420],fill=(70,48,30))
horse(928,392,0.98,0,stamp=True)
# kitchen bench with steam column bending
kx,ky=180,404
d.rectangle([kx,ky,kx+120,ky+10],fill=(110,80,50)); d.line([(kx+8,ky+10),(kx+8,ky+36)],fill=(110,80,50),width=5); d.line([(kx+112,ky+10),(kx+112,ky+36)],fill=(110,80,50),width=5)
for i in range(3):
    d.ellipse([kx+12+i*38,ky-12,kx+40+i*38,ky],fill=(222,216,200),outline=(150,140,120))
for i in range(22):
    t=i/26; sx=kx+58+math.sin(t*4)*10+t*26; sy=ky-16-t*96
    d.ellipse([sx-9+t*10,sy-5,sx+9-t*2,sy+5],fill=(245,244,238,110))
# long shadows toward building (light from left)
for (x,y,w) in [(352,352,120),(760,414,130),(520,420,90)]:
    d.polygon([(x,y),(x+w,y+4),(x+w+44,y+14),(x,y+10)],fill=(120,94,62,110))
# soften whole scene slightly for dawn air
from PIL import ImageFilter
img=img.filter(ImageFilter.GaussianBlur(0.6))
img.save(__file__.rsplit('/',1)[0]+'/intro-banner.png')
print('saved')
