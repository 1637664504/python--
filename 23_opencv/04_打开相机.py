''' 
查看相机
ls /dev/video*

'''
import sys
import cv2

def video_demo():
    number = 0
    if sys.argv[1]:
        number = int(sys.argv[1])

    # 0是代表摄像头编号，即默认打开 /dev/video0
    capture = cv2.VideoCapture(number)
    while (True):
        # 调用摄像机
        ref, frame = capture.read()
        # 输出图像,第一个为窗口名字
        cv2.imshow('frame', frame)
        # 10s显示图像，若过程中按“Esc”退出,若按“s”保存照片并推出
        c = cv2.waitKey(10) & 0xff
        if c == 27:
            # 简单暴力释放所有窗口
            cv2.destroyAllWindows()
            break
        elif c == ord('s'):
            # 储存照片
            cv2.imwrite('./images/pic.png',frame)
            break
 
 
if __name__ == '__main__':
    cv2.waitKey()
    video_demo()
