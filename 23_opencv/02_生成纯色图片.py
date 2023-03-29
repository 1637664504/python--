import time
import cv2
import numpy as np

wight = 25
hight = 50
img = np.zeros((hight,wight), np.uint8)
# 浅灰色背景
img.fill(255)
print(img)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imwrite("demo.png", img)