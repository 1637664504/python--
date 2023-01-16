import json
import requests
url='http://192.168.6.2:8090/'  #不存在的 ip:port,异常处理

try:
    x = requests.get(url)
except Exception as e:
    print("error ",e)
print('-----')

''' 
访问不存在的ip:port, get/post=都会异常
'''