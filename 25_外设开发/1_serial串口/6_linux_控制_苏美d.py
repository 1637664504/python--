''' 

'''
import time
import serial
import struct
import debugpy
from enum import Enum,IntEnum
from dataclasses import dataclass
from crc import Calculator,Crc16
from smd_data import *

class chassis_smd_data:
    ''' 苏美d 底盘数据协议 '''
    head0: int = 82 # 'R'
    head1: int = 69 # 'E'
    length: int = 2
    class _cmd(IntEnum):
        Data_RTK_INS: int       = 0x80  # RTK+INS输出数据
        Data_SLAM_LOCAL: int    = 0xC0  # SLAM输出位置和状态数据
        Data_SLAM_OBSTACLE: int = 0xC1  # SLAM输出障碍物信息数据
        Data_ASSIC: int         = 0x3F  # 配置、写 指令
    cmd = _cmd
    class _address_id(IntEnum):
        HOST_ID: int = 0x0
        NAV_ID: int = 0x5
        SLAM_LASER_ID: int = 0x18
        SLAM_VISION_ID: int = 0x19
    dst_id: _address_id
    src_id: _address_id

class Chassis_smd:
    def __init__(self,name,bps):
        self.serial = serial.Serial(name, bps, timeout=2)
        if self.serial.isOpen():
            print("Serial open ",self.serial.name)
        else:
            print("Serial error")
            raise Exception("serial 苏美d底盘打开失败")

        self.crc16_fun=Calculator(Crc16.CCITT,optimized=True)
        self.bflags = chassis_smd_data
    
    def connect_wifi(self,ssid,password):
        cmd = "#VSLAM SET WIFI,%s,%s;"%(ssid,password)
        self.serial.write(cmd.encode(encoding='utf-8'))

    def bytes_to_float(self,data) -> float:
        return float(struct.unpack('<f', struct.pack('4B', *data))[0])

    def handler_rtk_ins(self,data):
        var = data_rtk_ins
        var.pitch = struct.unpack("f",data[0:4])[0]
        var.roll = struct.unpack("f",data[4:8])[0]
        var.yaw = struct.unpack("f",data[8:12])[0]
        var.w = struct.unpack("f",data[12:16])[0]
        var.v = struct.unpack("f",data[16:20])[0]
        var.x = struct.unpack("i",data[20:24])[0]
        var.y = struct.unpack("i",data[24:28])[0]
        var.z = struct.unpack("i",data[28:32])[0]
        var.obs_range = [struct.unpack("i",data[32:36])[0],
                         struct.unpack("i",data[36:40])[0],
                         struct.unpack("i",data[40:44])[0],
                        #  struct.unpack("b",data[44]),
                         ]
        var.post_state = data[45]
        var.work_state = data[46]
        var.state = data[47]
        var.hall_L = struct.unpack("H",data[48:50])[0]
        var.hall_R = struct.unpack("H",data[50:52])[0]
        var.UL = data[52]
        var.UR = data[53]

    def handler_msg(self,data):
        if data[0] != self.bflags.head0 and data[1] != self.bflags.head1:
            return
        cmd = data[4]
        if cmd == self.bflags.cmd.Data_RTK_INS:
            self.handler_rtk_ins(data[7:])

    def pack_serial_frame(self,cmd,dst_id,src_id,b_data):
        frame = serial_frame
        frame.cmd = cmd
        frame.length = 5+len(b_data)  # cmd:1 dst_id:1 src_id:1 crc:2 = 5
        frame.dst_id = dst_id
        frame.src_id = src_id
        # frame.data = b_data
        b_head = struct.pack("ccHBBB",
                              frame.head0.encode(),
                              frame.head1.encode(),
                              frame.length,
                              frame.cmd,
                              frame.dst_id,
                              frame.src_id,
                              )

        frame.crc_16 = self.crc16_fun.checksum(b_head+b_data)
        b_crc = struct.pack("H",frame.crc_16)
        b_frame=b_head+b_data+b_crc
        return b_frame

    def pack_slam_data(self,data):
        b_data = struct.pack("fffffffBBBBfff",
                    data.x,
                    data.y,
                    data.z,
                    data.pitch,
                    data.roll,
                    data.yaw,
                    data.used_w,
                    data.slam_state,
                    data.map_state,
                    data.used1,
                    data.used2,
                    data.v,
                    data.w,
                    data.v
                )
        return b_data

    def show_hex(self,val):
        cnt = 0
        for i in val:
            print("%2x"%(i),end=' ')
            cnt+=1
            if cnt%16 == 0:
                print('--')

    def move_up(self,speed,direction=0):
        data = Data_slam
        # 速度值检测
        if speed > 30:
            speed = 30
        elif speed < -30:
            speed = -30
        
        # 方向值检测
        if direction > 30:
            direction = 30
        elif direction < -30:
            direction = -30

        data.v = speed
        data.w = direction
        b_data = self.pack_slam_data(data)
        b_frame = self.pack_serial_frame(Cmd.Data_SLAM_LOCAL,
                                         Address_id.NAV_ID,
                                         Address_id.Vision_Slam_ID,
                                         b_data)
        self.show_hex(b_frame)
        self.serial.write(b_frame)

    def get_cmd(self):
        while True:
            cmd = input("输入 w 前进")
            if cmd == 'w':
                self.move_up(10.0)
            elif cmd == 's':
                self.move_up(0.0)
            elif cmd == 'x':
                self.move_up(-10.0)
            elif cmd == 'q':
                self.move_up(10.0,-10.0)
            elif cmd == 'e':
                self.move_up(10.0,10.0)
            elif cmd == 'z':
                self.move_up(-10.0,-10.0)
            elif cmd == 'c':
                self.move_up(-10.0,10.0)
            else:
                print("不支持命令")
            time.sleep(3)
            self.move_up(0.0)

# 更简洁的写法
if __name__ == "__main__":
    serial_name = '/dev/ttyUSB0'
    bps = 115200
    ser = Chassis_smd(serial_name,bps)
    debugpy.listen(6688)
    
    # ssid="ruichizhihui-5G"
    # password = "zhihui1130"
    # ser.connect_wifi(ssid,password)
    # ser.set_frequency(2)
    # while True:
    #     data = ""
    #     if ser.serial.in_waiting:
    #         data = ser.serial.read(ser.serial.in_waiting)
    #         print("data len",len(data))
    #         print(data)
    #         ser.handler_msg(data)
    #         # ser.parse_msg(data)
    ser.get_cmd()

'''

'''
