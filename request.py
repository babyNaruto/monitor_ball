import requests
import json

url = 'http://127.0.0.1:8866/analysis/alarm_push'
data = {"name": "name"}

# 头部信息
headers = {'Content-Type': 'application/json'}

r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.text)
print(r.status_code)


