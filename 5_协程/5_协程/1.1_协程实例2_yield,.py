import time
def consumer():
    recvVal = ''
    while True:
        print("consumer 进入挂起")
        result = yield recvVal
        print("consumer 唤醒 获取值:%s" %(result))
        
        #发送协程返回值
        recvVal = '200 ok:%s' %(result)

def produce(coroutine):
    print("produce 启动")
    next(coroutine)     #启动协程
    sendData = 0
    while sendData < 5:
        sendData = sendData+1
        print("product 发送数据:%s,唤醒协程"% (sendData))
        ret = coroutine.send(sendData)
        print("product 收到数据:%s",ret)
        time.sleep(3)
    coroutine.close()

coroutine = consumer()
produce(coroutine)