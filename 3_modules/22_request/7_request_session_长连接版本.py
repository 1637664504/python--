import json
import requests

client = requests.session()
head = {'Connection': 'keep-alive'}
url = 'http://172.20.48.1:8080'
r=client.get(url,headers=head)
r=client.get(url,headers=head)
r=client.get(url,headers=head)
print(r.status_code)
print(r.text)