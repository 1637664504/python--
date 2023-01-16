# request post json格式数据 提交测试

import json
import requests
#url = 'http://192.168.6.1:8090/post' 自测有效
url = 'http://192.168.6.1:8090'
s = json.dumps({'key1': 'value1', 'key2': 'value2'})
head={'Content-Type':'application/json'}
print("text",s)
# r = requests.post(url, data=s,headers=head)
# print(r.text)
