#!/usr/bin/env python3
from PIL import Image,ImageDraw

#绘制线段
pic_a = Image.new('RGB',[200,200],'red')
draw = ImageDraw.Draw(pic_a)
draw.line([(0,0),(200,200)],fill='black',width=3)
draw.line([(0,100),(200,100)],fill='black',width=6)
pic_a.show()

#绘制点
pic_b = Image.new('RGB',[200,200],'white')
draw_b = ImageDraw.Draw(pic_b)
draw_b.point((50,50), fill='black')
pic_b.show()