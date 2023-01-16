import requests
import json
import time

a='''{
    "code": 0,
    "message": "success",
    "resp": {
        "focus_status": 1
    }
}'''
b=json.loads(a)
print(b)

#定位 字典数组
print(b['resp']['focus_status'])