
#!/usr/bin/env python3
#coding=utf-8
""" 
测试设备
    开发板: orangepi5
    i2c设备: R6082V imu 6轴传感器

验证 smbus2 API接口

"""
import time
from dataclasses import dataclass
from smbus2 import SMBus

@dataclass
class R6082V_i2c_param:
    Read_address:int = 0x38

i2c_id=1

with SMBus(i2c_id) as bus:
    # 读1B
    b = bus.read_byte_data(R6082V_i2c_param.Read_address, 0)
    print(b)

    # 读一段数据
    block = bus.read_i2c_block_data(R6082V_i2c_param.Read_address, 0, 4)
    print(block)

# 1.无权限错误
""" 
设置 i2c_id = 5
PermissionError: [Errno 13] Permission denied: '/dev/i2c-5'
"""

# 2.不存在设备
""" 
设置 i2c_id = 16
FileNotFoundError: [Errno 2] No such file or directory: '/dev/i2c-16'
"""

# 3.未挂载设备
""" 
设置 i2c_id = 5  #未挂载i2c设备

    ioctl(self.fd, I2C_SMBUS, msg)
OSError: [Errno 6] No such device or address
"""

# 4.地址错误
""" 
设置 i2c_id = 1 # 已挂载i2c设备
    Read_address:int = 0x38 # 错误的slave从设备地址

    ioctl(self.fd, I2C_SMBUS, msg)
OSError: [Errno 6] No such device or address
"""