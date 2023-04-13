''' 

# 打开 COM17，将波特率配置为115200，数据位为7，停止位为2，无校验位，读超时时间为0.5秒。
ser = serial.Serial(port="COM17",
                    baudrate=115200,
                    bytesize=serial.SEVENBITS,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_TWO,
                    timeout=0.5) 

'''

import serial

serial_name = 'COM11'
bps=115200
# try:
#     ser = serial.Serial(serial_name,bps)
#     if ser.isOpen():
#         print("Serial open")
#         print("serial_name",ser.name)
# except Exception as e:
#     print("Serial error:",e)

# 方法2： 更简洁的写法
with serial.Serial(serial_name,bps) as serial:
    if serial.isOpen():
        print("Serial open ",serial.name)
    else:
        print("Serial error")

''' 
需要class 支持  __enter__ 和 __exit__ 方法
__enter__ : 然后执行 with 语句中的代码
__exit__ : 调用 __exit__ 方法，退出或异常 会关闭文件流。
'''
