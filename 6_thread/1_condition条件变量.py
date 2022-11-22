import threading
import time
import sys

# 商品
zoom_status=''
zoom_value=1
# 条件变量
con = threading.Condition(threading.Lock())

def demo_help():
    print('cmd: in, out , stop')

# 生产者方法
def produce():
    global zoom_status
    global zoom_value

    while True:
        con.acquire()
        if zoom_status == 'stop':
            con.wait()
            print('zoom_status = ',zoom_status)
        
        if zoom_status == 'in':
            zoom_value -= 0.1
            if zoom_value < 1.0:
                zoom_value = 1.0
            print('缩小 zoom:',zoom_value)
        elif zoom_status == 'out':
            zoom_value += 0.1
            if zoom_value > 17.5:
                zoom_value = 17.5
            print('放大 zoom:',zoom_value)

        con.wait(0.1)
        con.release()


# 消费者方法
def consume():
    global zoom_status
    global zoom_value
    val=''
    while True:
        val = input()
        if val == 'exit':
            sys.exit(0)
        elif (val == 'in') or (val == 'out') or (val == 'stop'):
            if zoom_status == val:
                continue
            con.acquire()
            zoom_status = val
            con.notify()
            con.release()
        else:
            print('cmd not support')
            demo_help()
            

t2 = threading.Thread(target=consume)
t2.start()
t1 = threading.Thread(target=produce)
t1.start()
