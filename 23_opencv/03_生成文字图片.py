import time
import cv2
import numpy as np

wight = 500
hight = 100
img = np.zeros((hight,wight), np.uint8)
# 浅灰色背景
img.fill(255)

#
text = time.strftime('%Y%m%d-%H%M%S', time.localtime())
info = "pitch=30,zoom=5.0"
cv2.putText(img, text, (30, 30), cv2.FONT_HERSHEY_COMPLEX, 1.0, (100, 0, 0), 1)
cv2.putText(img, info, (30, 60), cv2.FONT_HERSHEY_COMPLEX, 1.0, (100, 0, 0), 1)

print(img)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imwrite("3_demo.png", img)

''' 
格式
cv2.putText(src, text, place, Font, Font_Size, Font_Color, Font_Overstriking)
实例
cv2.putText(img, text, (30, 30), cv2.FONT_HERSHEY_COMPLEX, 1.0, (100, 0, 0), 1)

参数解释
src	        输入图像
text	    需要添加的文字
place	    左上角坐标
Font	    字体类型
Font_Size	字体大小
Font_Color	文字颜色
Font_Overstriking	字体粗细
'''