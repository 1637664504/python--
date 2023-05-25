
#!/usr/bin/env python3
#coding=utf-8
""" 
测试设备
    开发板: orangepi5
    i2c设备: R6082V imu 6轴传感器

验证
    读取完整的R6082V imu数据


python依赖
    pip3 install crccheck
"""
import time
import struct
from dataclasses import dataclass
from smbus2 import SMBus
from crccheck.checksum import Checksum16,Checksum8

@dataclass
class R6082V_i2c_param:
    Read_address: int = 0x35
    Write_address: int = 0x35
    Data_len: int = 22

class R6082V_data:
    yaw: float
    yaw_rate: float
    checksum_a: int
    roll: float
    pitch: float
    roll_rate: float
    pitch_rate: float
    x_acc: float
    y_acc: float
    z_acc: float
    index: int
    checksum_b: int

class R6082V_Imu:
    def __init__(self,devname):
        index = devname[-1]
        if not index.isdigit():
            print("请输入正确的i2c设备")
            raise Exception("请输入正确的i2c设备")

        self.bus = SMBus(int(index))
        data = self.bus.read_byte_data(R6082V_i2c_param.Read_address,0)
        print("打开i2c:%s index=%d,读取到数据:" %(devname,int(index)))
        print("data:",data)

        self.devname = devname
        self.data = R6082V_data()
        self.recv_data = b''
    
    def sync_read(self):
        self.recv_data = self.bus.read_i2c_block_data(R6082V_i2c_param.Read_address, 0, R6082V_i2c_param.Data_len)
        print("recv len",len(self.recv_data))

    def data_to_float(self,msb,lsb):
        var = struct.pack(">BB",msb,lsb)
        ret = struct.unpack(">h",var)[0]/100
        return ret

    def parse_msg(self):
        recv = self.recv_data
        var = self.data

        var.yaw = self.data_to_float(recv[0],recv[1])
        var.yaw_rate = self.data_to_float(recv[2],recv[3])
        var.checksum_a = ((recv[4]<<8) | recv[5])
        var.roll = self.data_to_float(recv[6],recv[7])
        var.pitch = self.data_to_float(recv[8],recv[9])
        var.roll_rate = self.data_to_float(recv[10],recv[11])
        var.pitch_rate = self.data_to_float(recv[12],recv[13])
        var.x_acc = self.data_to_float(recv[14],recv[15])
        var.y_acc = self.data_to_float(recv[16],recv[17])
        var.z_acc = self.data_to_float(recv[18],recv[19])
        var.index = recv[20]
        var.checksum_b = recv[21]
        print("yaw:%.2f roll:%.2f pitch:%.2f,rate y:%.2f r:%.2f p:%.2f,acc x:%.2f y:%.2f z:%.2f ,sum %x %x %d"
              %(var.yaw,var.roll,var.pitch,
                var.yaw_rate,var.roll_rate,var.pitch_rate,
                var.x_acc,var.y_acc,var.z_acc,
                var.checksum_a,var.checksum_b,var.index))
        # ret_a = Checksum16.calc(recv[0:4])
        # ret_b = Checksum8.calc(recv[6:21])
        # print("ret_a=%x,ret_b=%x"%(ret_a,ret_b))

if __name__ == "__main__":
    imu_impl = R6082V_Imu('/dev/i2c-1')
    while True:
        imu_impl.sync_read()
        imu_impl.parse_msg()
        time.sleep(0.4)

