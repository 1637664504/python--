import _thread
import time
def bms_send_read_cmd(threadName,args):
    print(threadName," ",args)
    return 0

idx = 10
try:
   _thread.start_new_thread(bms_send_read_cmd, ("Thread-1", idx) )
except:
   print ("Error: 无法启动线程")

time.sleep(10)