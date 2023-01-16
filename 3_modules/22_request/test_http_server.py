#!/usr/bin/env python3
import requests
import json

url = "http://127.0.0.1:8888/v1/camera/photo/control"

payload = json.dumps({
  "req": {
    "device_id": 0,
    "start_flag": 0,
    "storage_folder": "",
    "storage_file_name": "test_8"
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)