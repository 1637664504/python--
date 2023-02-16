import threading
import time

def fun_a():
    n=0
    while n<10:
        print("fun_a a",n)
        time.sleep(1)
        n+=1

def fun_b():
    n=0
    while n<10:
        print("fun_b b",n)
        time.sleep(0.5)
        n+=1

t2 = threading.Thread(target=fun_a)
t1 = threading.Thread(target=fun_b)
t1.start()
t2.start()

t1.join()
t2.join()
print("end")
