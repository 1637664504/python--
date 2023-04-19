
from enum import Enum,IntEnum
from dataclasses import dataclass

@dataclass
class SMD_flags:
    head0: int = ord('R')
    head1: int = ord('E')
    length: int = 0
    class _cmd(IntEnum):
        Data_RTK_INS: int       = 0x80  # RTK+INS输出数据
        Data_SLAM_LOCAL: int    = 0xC0  # SLAM输出位置和状态数据
        Data_SLAM_OBSTACLE: int = 0xC1  # SLAM输出障碍物信息数据
        Data_ASSIC: int         = 0x3F  # ASSIC
    cmd = _cmd
