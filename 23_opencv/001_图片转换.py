# jpg 转 png
import os
import cv2
file = '20221206-111145-4579191.jpg'
im = cv2.imread(file)
output_path = ''
if output_path:
    cv2.imwrite(os.path.join(output_path, file.replace('jpg', 'png')), im,7)
else:
    cv2.imwrite('1.png', im,  [int( cv2.IMWRITE_JPEG_QUALITY), 90])
