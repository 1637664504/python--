import threading
import time

interval_time = 2
def fun_timer_test():
    print("time ",time.time())
    global interval_time
    timer = threading.Timer(2,fun_timer_test)
    timer.start()

timer = threading.Timer(2,fun_timer_test)
timer.start()
print("end")
''' 
'''