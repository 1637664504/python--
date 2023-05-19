#!/usr/bin/env python3
#coding=utf-8
""" 
imu R6082V模块 UART 数据解析
上报imu数据
"""
import serial
import struct
from dataclasses import dataclass

@dataclass
class R6082V_Const:
    Frame_Len: int = 15

class R6082V_frame(Virtual_Imu_impl):
    head0: int = 0xAA
    head1: int = 0x00
    index: int
    yaw: float
    yaw_acc: float      # yaw 角速度
    roll: float
    pitch: float
    acc_x: int
    reserved: int
    checksum: int

class Imu_R6082V:
    def __init__(self,name,bps):
        self.serial = serial.Serial(name, bps, timeout=5)
        if self.serial.isOpen():
            print("Serial open ",self.serial.name)
        else:
            print("Serial error")
            raise Exception("R6082V serial %s 打开失败")%(name)

        self.frame = R6082V_frame()
        self.recv_data = b''
        self.print_count: int = 0

    def bin_to_float(self,B):
        ret = struct.unpack("<h",B)[0]
        ret = round(ret/100,2)
        return ret

    def sync_read(self):
        ret = False

        self.recv_data = ser.serial.read(R6082V_Const.Frame_Len)
        if len(self.recv_data) == R6082V_Const.Frame_Len:
            ret = True
        else:
            print("not read")
            raise Exception("读取serial异常")
        return ret

    def parse_msg(self):
        msg = self.recv_data
        if len(msg) != 15 or \
            msg[13] != 0x55 or \
            (msg[0] != self.frame.head0 or msg[1] != self.frame.head1):
            print("报文校验不通过")
            return False
        self.frame.index = msg[2]
        self.frame.yaw = self.bin_to_float(msg[3:5])
        self.frame.yaw_acc = self.bin_to_float(msg[5:7])
        self.frame.roll = self.bin_to_float(msg[7:9])
        self.frame.pitch = self.bin_to_float(msg[9:11])
        self.frame.acc_x = self.bin_to_float(msg[11:13])
        self.frame.reverse = msg[13]
        self.frame.checksum = msg[14]

        # if True:
        if (int(self.print_count%50) == 0):
            print("yaw:%f roll:%f pitch:%f\n yaw_acc=%f acc=%f recv=%x sum=%d" %
                (self.frame.yaw, self.frame.roll, self.frame.pitch,
                self.frame.yaw_acc, self.frame.acc_x, self.frame.reverse, self.frame.checksum
                ))
            print_count = 1
        self.print_count += 1

        """ 
        hal imu impl功能实现
        """
        # def hal_get_imu_data(self):
        #     pass
        # def hal_set_rate(rate):
        #     pass

# 更简洁的写法
if __name__ == "__main__":
    # serial_name = 'COM17'
    serial_name = '/dev/ttyUSB0'
    bps = 115200
    ser = Imu_R6082V(serial_name,bps)

    while True:
        if ser.sync_read():
            ser.parse_msg()