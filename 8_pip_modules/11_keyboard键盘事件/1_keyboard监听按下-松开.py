import keyboard


def callback(x):
    print(x)
    print()


keyboard.hook(callback)
# 按下任何按键时，都会调用callback，其中一定会传一个值，就是键盘事件
keyboard.wait()
