''' 
IMU RTK FS982模块数据解析
串口数据协议解析
'''
#!/usr/bin/python3
#coding=utf-8

import time
import serial
import struct
from dataclasses import dataclass
from crc import Calculator,Crc32

# debug
import debugpy

from bytesConvert import *

# ros
# import rospy
# from sensor_msgs.msg import Imu

@dataclass
class FS982AG_Constan:
    Head1: int = 0xaa
    Head2: int = 0x55
    Frame_id: int = 0x166
    # Frame_len: int = 0x32

class FS982AG_frame:
    head1: int
    head2: int
    frame_id: int
    frame_len: int
    gps_itow: int           #GPS周内毫秒
    gps_week_num: int       #GPS周计数
    lat: int                #纬度 纬度的值是lat除以10的7次方 double lat=((double)nav_struct.lat)/10000000.0;
    lon: int                #经度 经度的值是lon除以10的7次方 double lon=((double)nav_struct.lon)/10000000.0;
    hight: int              #高度 高度的值是除以10的3次方 double hgt=((double)nav_struct.hgt)/1000.0;
    vn: float               #北向速度
    ve: float               #东向速度
    vd: float               #地向速度
    roll: float
    pitch: float
    yaw: float
    rtk_yaw: float          #双天线航向
    unsed1: float
    acc_x: float            # 加速度
    acc_y: float
    acc_z: float
    gyroscope_x: float      # 陀螺仪
    gyroscope_y: float
    gyroscope_z: float
    temp: float             #温度
    fix_type: int           #定位状态
    sv_num: int             #星数
    diff_age: int           #差分延时
    heading_type: int       #定向状态
    pos_acc: int            #位置精度因子 cm
    status: int             #状态位
    rev1: int
    rev2: int
    crc: int

class Imu_FS982AG:
    def __init__(self,config):
        self.config = config
        self.init_data()
        self.open_serial(self.config['devname'], self.config['bps'],2)
        self.calculator32 = Calculator(Crc32.CRC32, optimized=False)

        cmd="AT+OUTRATE=50\r\n"
        self.serial.write(cmd.encode())
        cmd="AT+SETNAV\r\n"
        self.serial.write(cmd.encode())
        cmd="AT+SAVE\r\n"
        self.serial.write(cmd.encode())
        
    def open_serial(self, devname, bps, timeout):
        self.serial = serial.Serial(devname, bps, timeout=timeout)
        if self.serial.isOpen():
            print("Serial open ",devname)
        else:
            print("Serial error",devname)

    def init_data(self):
        self.recv = b''
        self.frame: FS982AG_frame = FS982AG_frame()

    def verify_rtk_head(self,recv):
        if len(recv) < 2:
            print("数据太少 不是rtk数据,len=",len(recv))
            return False

        if recv[0] == FS982AG_Constan.Head1 and recv[1] == FS982AG_Constan.Head2:
            # and bytes_to_uint16(recv[2:4]) == FS982AG_Constan.Frame_id:
            # length = bytes_to_uint16(data[4:6])
            # print("read ok id=0xAA len=0x%X recv_len:%u"%(length,len(data)))
            print("read ok ")
            return True
        else:
            print("rtk head检验不通过")

        return False

    def read_rtk_frame(self):
        recv = b''
        while True:
            if self.serial.in_waiting:
                recv = self.serial.read(self.serial.in_waiting)
                if self.verify_rtk_head(recv):
                    recv += self.serial.read(104-len(recv))
                    break
        self.recv = recv

    def parse_msg(self):
        var = self.frame
        data = self.recv
        var.frame_id = bytes_to_uint16(data[2:4])
        var.frame_len = bytes_to_uint16(data[4:6])
        if var.frame_id != FS982AG_Constan.Frame_id and var.frame_len != 0x5e:
            print("校验帧id len 不通过")
            return

        # GPS信息
        var.gps_itow = bytes_to_uint32(data[6:10])
        var.gps_week_num = bytes_to_uint16(data[10:12])
        var.lat = bytes_to_uint32(data[12:16])/10000000
        var.lon = bytes_to_uint32(data[16:20])/10000000
        var.hight = bytes_to_uint32(data[20:24])/1000
        var.vn = bytes_to_float32(data[24:28])
        var.ve = bytes_to_float32(data[28:32])
        var.vd = bytes_to_float32(data[32:36])
        
        # IMU信息
        var.roll = bytes_to_float32(data[36:40])
        var.pitch = bytes_to_float32(data[40:44])
        var.yaw = bytes_to_float32(data[44:48])
        var.rtk_yaw = bytes_to_float32(data[48:52])
        # var.unsed1 = bytes_to_float32(data[52:56])
        var.acc_x = bytes_to_float32(data[56:60])
        var.acc_y = bytes_to_float32(data[60:64])
        var.acc_z = bytes_to_float32(data[64:68])
        var.gyroscope_x = bytes_to_float32(data[68:72])
        var.gyroscope_y = bytes_to_float32(data[72:76])
        var.gyroscope_z = bytes_to_float32(data[76:80])
        var.temp = bytes_to_float32(data[80:84])
        
        # RTK配置信息
        var.fix_type = data[84]
        var.sv_num = data[85]
        var.diff_age = data[86]
        var.heading_type = data[87]
        var.pos_acc = bytes_to_uint16(data[88:90])
        var.status = bytes_to_uint16(data[90:92])
        
        # crc
        # cal_crc = self.calculator32.checksum(data[0:100])
        # recv_rcr = bytes_to_uint32(data[100:104])
        # print("cal crc=%x recv_crc=%x"%(cal_crc,recv_rcr))

    def show_info(self):
        var = self.frame
        print("RTK gps时间week:%u-%u  经纬lat:%f lon:%f hig:%f 方向速度:北%f 东%f 地向%f"%(
            var.gps_week_num, var.gps_itow,
            var.lat, var.lon, var.hight,
            var.vn, var.ve, var.vd
            ))
        print("IMU roll:%f pitch:%f yaw:%f acc x:%f y:%f z:%f gyr x:%f y:%f z:%f temp:%f"%(
            var.roll, var.pitch, var.yaw,
            var.acc_x, var.acc_y, var.acc_z,
            var.gyroscope_x, var.gyroscope_y, var.gyroscope_z,
            var.temp
            ))
        print("GPS配置 定位解:%u 星数:%u 差分延时:%u 定向状态:%u 位置精度因子:%u 状态:%X"%(
            var.fix_type, var.sv_num, var.diff_age,
            var.heading_type, var.pos_acc, var.status
            ))

    def loop_run(self):
        while True:
            self.read_rtk_frame()
            self.parse_msg()
            self.show_info()

# 更简洁的写法

if __name__ == "__main__":

    config={
        'devname': "COM21",
        'bps': 115200,
    }
    debugpy.listen(6688)
    # debugpy.wait_for_client()
    # debugpy.breakpoint()
    tty = Imu_FS982AG(config)
    tty.loop_run()
        