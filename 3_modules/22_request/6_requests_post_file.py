import json
import requests
URL='http://192.168.6.2:8080/'
files = {'file': open('1.txt', 'rb')}
head = {'Content-Type':'binary'}
requests.post(url=URL,files=files,headers=head)