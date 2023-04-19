from enum import Enum,IntEnum
from dataclasses import dataclass

@dataclass
class Cmd(IntEnum):
    Data_RTK_INS: int       = 0x80  # RTK+INS输出数据
    Data_SLAM_LOCAL: int    = 0xC0  # SLAM输出位置和状态数据
    Data_SLAM_OBSTACLE: int = 0xC1  # SLAM输出障碍物信息数据
    Data_ASSIC: int         = 0x3F  # ASSIC

@dataclass
class Address_id(IntEnum):
    ''' 设备地址 '''
    Host_ID: int = 0x00
    NAV_ID: int = 0x05
    Laser_Slam_ID: int = 0x18
    Vision_Slam_ID: int = 0x19

@dataclass
class serial_frame:
    '''数据帧协议格式'''
    head0 = 'R'
    head1 = 'E'
    length: int = 0
    cmd: int = Cmd.Data_ASSIC
    dst_id: int = Address_id.Vision_Slam_ID
    src_id: int = Address_id.NAV_ID
    data: bytes = b''
    crc_16: int = 0

class Mower_state(IntEnum):
    Mower_standby_state     = 0
    Mower_cutting_state     = 1
    Mower_home_state        = 2
    Mower_home_charge_state = 3
    Mower_charge_state      = 4
    Mower_charge_start_state    = 5
    Mower_trimming_state    = 6
    Mower_wait_state        = 7
    Mower_manual_state      = 8

class data_rtk_ins:
    pitch: float
    roll: float
    yaw: float
    w: float        # 角速度 弧度/s
    v: float        # 水平移动速度 cm/s
    x: int # x position
    y: int # y position
    z: int # z position
    obs_range: int = [0,0,0,0]  # 障碍物探测范围 cm
    post_state=0  # 定位转台信息
    work_state=0  # 工作状态
    state=0   # 状态信息
    hall_L=0  # 左编码计数
    hall_R=0  # 右编码计数
    UL=0      # 距离范围0-127cm，最高位判断是否触发超声波，0：不触发  1 ：触发
    UR=0      # 距离范围0-127cm，最高位判断是否触发超声波，0：不触发  1 ：触发

class Slam_state(IntEnum):
    Slam_local_lost     = 0
    Slam_reserve        = 1
    Slam_local_available    = 2
    Slam_map_state      = 3

class Map_state(IntEnum):
    Start_map       = 0
    Building_map    = 1
    Finish_map      = 2
    Map_available   = 3
    Map_unavailable = 4
    No_map          = 5

@dataclass
class Data_slam:
    x: float        = 0.0
    y: float        = 0.0
    z: float        = 0.0
    pitch: float    = 0.0
    roll: float     = 0.0
    yaw: float      = 0.0
    used_w: float   = 0.0
    slam_state: int = Slam_state.Slam_local_lost
    map_state: int  = Map_state.No_map
    used1: int      = 0
    used2: int      = 0
    v: float        = 0.0   # 线速度 -30~30 cm/s
    w: float        = 0.0   # 角速度 -30~30 deg/s
    x: float        = 0.0   # 备用
