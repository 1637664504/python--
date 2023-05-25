''' 

'''

import serial
import struct
from dataclasses import dataclass
from crc import Calculator,Crc16

@dataclass
class CH0X0_Constan:
    MsgLen: int = 82

class CH0X0_data:
    tag: bytes = 0x91       # 包标签
    reserve1: bytes = 0x0
    reserve2: bytes = 0x0
    tempertaure: int        # 温度
    pressure: float         # 气压
    time: int               # 时间戳
    accelerometer_x: float  # 加速度
    accelerometer_y: float
    accelerometer_z: float
    gyroscope_x: float      # 陀螺仪
    gyroscope_y: float
    gyroscope_z: float
    magnetometer_x: float   # 磁场计
    magnetometer_y: float
    magnetometer_z: float
    euler_x: float          # 欧拉角、姿态角
    euler_y: float
    euler_z: float
    quaternion_w: float     # 四元组
    quaternion_x: float
    quaternion_y: float
    quaternion_z: float

class serial_CH0X0:
    def __init__(self,name,bps):
        self.serial = serial.Serial(name, bps, timeout=2)
        if self.serial.isOpen():
            print("Serial open ",self.serial.name)
        else:
            print("Serial error")
            raise Exception("serial CH0X0 打开失败")

        self.byte_flag={
            'frame_header': 0x5A,
            'frame_type':   0xA5,
        }
        self.data = CH0X0_data
        self.crc16_fun=Calculator(Crc16.CCITT,optimized=True)

    def serial_reset(self):
        cmd = b'AT+RST\r\n'
        self.serial.write(cmd)

    def set_frequency(self,var: int):
        # 设置串口输出频率
        cmd ='AT+ODR=%d\r\n'%(var)
        cmd_data = cmd.encode()
        self.serial.write(cmd_data)
        self.serial_reset()

    def parse_tempertaure(self,data):
        self.data.tempertaure = data[3]
        print("温度%d",self.data.tempertaure)

    def bytes_to_float(self,data) -> float:
        return float(struct.unpack('<f', struct.pack('4B', *data))[0])

    def parse_accelerometer(self,data):
        self.data.accelerometer_x = self.bytes_to_float(data[12:16])
        self.data.accelerometer_y = self.bytes_to_float(data[16:20])
        self.data.accelerometer_z = self.bytes_to_float(data[20:24])
        print("加速度 x=%f,y=%f,z=%f"%(self.data.accelerometer_x,self.data.accelerometer_y,self.data.accelerometer_z))

    def parse_gyroscope(self,data):
        self.data.gyroscope_x = self.bytes_to_float(data[24:28])
        self.data.gyroscope_y = self.bytes_to_float(data[28:32])
        self.data.gyroscope_z = self.bytes_to_float(data[32:36])
        print("陀螺仪 x=%f,y=%f,z=%f"%(self.data.gyroscope_x,self.data.gyroscope_y,self.data.gyroscope_z))

    def parse_magnetometer(self,data):
        self.data.magnetometer_x = self.bytes_to_float(data[36:40])
        self.data.magnetometer_y = self.bytes_to_float(data[40:44])
        self.data.magnetometer_z = self.bytes_to_float(data[44:48])
        print("磁场计 x=%f,y=%f,z=%f"%(self.data.magnetometer_x,self.data.magnetometer_y,self.data.magnetometer_z))

    def parse_euler(self,data):
        self.data.euler_x = self.bytes_to_float(data[48:52])
        self.data.euler_y = self.bytes_to_float(data[52:56])
        self.data.euler_z = self.bytes_to_float(data[56:60])
        print("欧拉角 x=%f,y=%f,z=%f"%(self.data.euler_x,self.data.euler_y,self.data.euler_z))

    def parse_quaternion(self,data):
        self.data.quaternion_w = self.bytes_to_float(data[60:64])
        self.data.quaternion_x = self.bytes_to_float(data[64:68])
        self.data.quaternion_y = self.bytes_to_float(data[68:72])
        self.data.quaternion_z = self.bytes_to_float(data[72:76])
        print("四元组 w=%f,x=%f,y=%f,z=%f"%(self.data.quaternion_w,self.data.quaternion_x,self.data.quaternion_y,self.data.quaternion_z))

    def parse_msg(self,msg):
        if msg[0] == self.byte_flag['frame_header'] and msg[1] == self.byte_flag['frame_type']:
            msg_len = msg[2] + (msg[3] << 8)
            crc_sum = msg[4] + (msg[5] << 8)
            crc_buf = msg[0:4] + msg[6:]
            cal_crc_sum = self.crc16_fun.checksum(crc_buf)
            print("crc",crc_sum,cal_crc_sum)
            if crc_sum == cal_crc_sum:
                data = msg[6:]
                self.parse_tempertaure(data)
                self.parse_accelerometer(data)
                self.parse_gyroscope(data)
                self.parse_magnetometer(data)
                self.parse_euler(data)
                self.parse_quaternion(data)

    def check_imu_head(self,msg):
        if msg[0] == self.byte_flag['frame_header'] and msg[1] == self.byte_flag['frame_type']:
            return True
        
        return False

# 更简洁的写法
if __name__ == "__main__":
    serial_name = 'COM18'
    bps = 115200
    ser = serial_CH0X0(serial_name,bps)
    ser.set_frequency(2)
    read_len: int = 0
    while True:
        data = ""
        if ser.serial.in_waiting:
            data = ser.serial.read(ser.serial.in_waiting)
            print("data len",len(data))
            read_len = len(data)
            if ser.check_imu_head(data):
                data2 = ser.serial.read(82-read_len)
                data += data2
                ser.parse_msg(data)
            else:
                read_len = 0
                print("not imu head. Drop !!!")

'''

'''
