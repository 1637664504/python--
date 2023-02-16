import threading
import time

def fun_a(args):
    n=0
    print(type(args))
    while n<100:
        print("fun_a ",args," a",n)
        time.sleep(1)
        n+=1

def fun_b(args):
    n=0
    var = args[0]
    print(type(var))
    while n<100:
        print("fun_b ",var," b",n)
        time.sleep(0.5)
        n+=1

#传递参数, 列表自动转换为 参数
t1 = threading.Thread(target=fun_a, args=[1])
t2 = threading.Thread(target=fun_b, args=['bbb'])
# t1 = threading.Thread(target=fun_b, args=(2,))
# t2 = threading.Thread(target=fun_a, args=('aaa',))
t1.start()
t2.start()

t1.join()
t2.join()
print("end")

''' 
<class 'int'>
fun_a  1  a 0
<class 'str'>
fun_b  b  b 0 
'''