#!/usr/bin/env python3
from PIL import Image,ImageDraw,ImageFont
pic_a = Image.new('RGB',[200,200],'red')

#linux查看支持得字体: fc-list
font = ImageFont.truetype('FreeMonoBold.ttf',16)
draw = ImageDraw.Draw(pic_a)

draw.text((100,100),'hello world',font=font,fill='black')
pic_a.show()