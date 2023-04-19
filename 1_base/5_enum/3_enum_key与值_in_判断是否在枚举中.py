''' 
Python enum 枚举
判断 key(键) 或者 value(值)是否在枚举中
'''
from enum import Enum,IntEnum
class _address_id(IntEnum):
    HOST_ID: int = 0x0
    NAV_ID: int = 0x5
    SLAM_LASER_ID: int = 0x18
    SLAM_VISION_ID: int = 0x19
    
a=0x18

if "HOST_ID" in _address_id.__members__:
    print("11111111111")
if a in _address_id._value2member_map_:
    print("2222222222")

print("++++")

''' 
11111111111
2222222222
++++
'''