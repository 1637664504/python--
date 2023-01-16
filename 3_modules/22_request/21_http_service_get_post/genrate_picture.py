#!/usr/bin/env python3
from PIL import Image,ImageDraw,ImageFont
import random
import time

def generate_verif_code(fileName):
    pic_a = Image.new('RGB',[200,200],'white')
    #linux查看支持得字体: fc-list
    font = ImageFont.truetype('FreeMonoBold.ttf',16)
    draw = ImageDraw.Draw(pic_a)

    # file=time.strftime('%Y%m%d-%H%M%S', time.localtime())+'.png'
    file = fileName+'png'
    capthca_str=str(random.randint(1000,9999))
    draw.text((80,90),capthca_str,font=font,fill='black')
    pic_a.save(file,format='png')