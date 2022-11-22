# 导入 requests 包
import requests

# 发送请求
# x = requests.get('https://www.runoob.com/')
# x = requests.get('https://www.runoob.com/')
# x = requests.get('https://www.runoob.com/')
# x = requests.get('https://www.runoob.com/')
x = requests.get('http://127.0.0.1:8080')
x = requests.get('http://127.0.0.1:8080')
x = requests.get('http://127.0.0.1:8080')
# 返回网页内容
print(x.text)