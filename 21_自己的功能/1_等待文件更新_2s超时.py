''' 
需求:
如果文件不存在,用2s超时判断是否存在
'''
import time
import os

test_file = '/home/liuj/1_Data/3_python_example/21_自己的功能/2.txt'
timeout = 0.0
while True:
    if os.path.exists(test_file) == True:
        break
    time.sleep(0.5)
    timeout += 0.5
    if timeout >= 2.0:
        break
    