#!/usr/bin/env python3
from PIL import Image

pic_a = Image.new('RGB',(360,240),(255,255,255))
pic_a.save('white.png',format='png')

pic_b = Image.new('RGB',(360,240),(0,0,0))
pic_b.save('black.png',format='png')