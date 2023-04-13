''' 
查看已有的 serial 串口设备
pip3 install pyserial
'''
import serial
import serial.tools.list_ports

ports_list = list(serial.tools.list_ports.comports())
print(ports_list)
for its in ports_list:
    print(its.description,its.device)

''' 
[<serial.tools.list_ports_common.ListPortInfo object at 0x0000019D5C024DF0>, <serial.tools.list_ports_common.ListPortInfo object at 0x0000019D5C078310>, <serial.tools.list_ports_common.ListPortInfo object at 0x0000019D5C078790>]
通信端口 (COM1) COM1
USB-SERIAL CH340 (COM9) COM9
Silicon Labs CP210x USB to UART Bridge (COM11) COM11
'''