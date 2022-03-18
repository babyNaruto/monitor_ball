import requests
import os

def push_img(alarm_img_name,alarm_img_url):
    url = "http://127.0.0.1:8866/analysis/alarm_push/"

    payload = {}

    files = [
        ('image', (alarm_img_name, open(alarm_img_url, 'rb'), 'image/jpeg'))
    ]
    headers = {
        'Content-Type': 'image/jpeg',
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print('response success')
def alarm_push_info()
url = 'http://127.0.0.1:8866/analysis/alarm_push'
data = {"name": "name"}

# 头部信息
headers = {'Content-Type': 'application/json'}

r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.text)
print(r.status_code)
