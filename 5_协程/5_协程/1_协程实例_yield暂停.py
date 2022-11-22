import time
def consumer():
    ret = ''
    while True:
        print('consumer 挂起')
        result = yield ret
        print("consumer 恢复 获取值:",result)
        ret = '200 ok'

def produce(coroutine):
    print('product 启动协程')
    next(coroutine)
    sendData = 0
    while sendData < 5:
        sendData = sendData+1
        print('produce 发送数据 %s'  %(sendData))
        result = coroutine.send(sendData)
        print('product 获取结果 %s' %(result))
        time.sleep(5)
    coroutine.close()

coroutine = consumer()
produce(coroutine)