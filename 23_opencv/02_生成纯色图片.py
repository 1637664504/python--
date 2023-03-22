import cv2
import numpy as np

img = np.zeros((10, 10), np.uint8)
# 浅灰色背景
img.fill(255)
cv2.imshow('img', img)
cv2.waitKey(0)