# 验证: IntEnum 可以与 数值直接判断
from enum import IntEnum
class Shape(IntEnum):
    Circle = 1
    Square = 2

if Shape.Circle == 1:
    print("Circle -----")

''' 
IntEnum 可以与 数值直接判断
Circle -----
'''