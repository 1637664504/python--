#!/usr/bin/env python3
import time
def consumer(name,max):
    print('consumer %s 要吃100个饺子' %(name))
    sum=0
    while True:
        print("consumer %s 等待饺子" %(name))
        bread_num = yield
        sum+=bread_num
        print('consumer 获得: %d个饺子,总共吃了:%d'%(bread_num,sum))
        if sum >= max:
            break
    print('顾客 %s 吃饱了'%(name))
        
def producer(cop):
    cop.send(None)
    n = 0
    while n<10:
        print('厨师:煮好了10个饺子')
        cop.send(10)
        print('厨师:需要1min分钟,才能包好10个饺子')
        time.sleep(2)
        n+=1
        
if __name__ == '__main__':
    cop = consumer('老王',100)
    producer(cop)
