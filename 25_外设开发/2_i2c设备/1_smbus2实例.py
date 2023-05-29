
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
    Read_address:int = 0x35

with SMBus(1) as bus:
    # 读1B
    b = bus.read_byte_data(R6082V_i2c_param.Read_address, 0)
    print(b)

    # 读一段数据
    block = bus.read_i2c_block_data(R6082V_i2c_param.Read_address, 0, 4)
    print(block)

    # 写数据
    zero = 0x00
    bus.write_byte_data(R6082V_i2c_param.Read_address,0,zero)

    # 写一段数据
    attitude_reset = [0x00,0x00]        #姿态重置
    bus.write_i2c_block_data(R6082V_i2c_param.Read_address,0,attitude_reset)

    time.sleep(2)
    # 读一段数据
    block = bus.read_i2c_block_data(R6082V_i2c_param.Read_address, 0, 4)
    print(block)
