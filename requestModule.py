import requests
import os
import json

import share_data
from share_data import GlobalRequest


# 告警图片推送
def push_img(alarm_img_name, alarm_img_url):
    url = "http://127.0.0.1:8806/analysis/alarm_push/"

    payload = {}

    files = [
        ('image', (alarm_img_name, open(alarm_img_url, 'rb'), 'image/jpeg'))
    ]
    headers = {
        'Content-Type': 'image/jpeg',
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.status_code)
    print('response success')
    print(response.text)


# 告警信息推送
def alarm_push_info(**alarm_info):
    url = 'http://127.0.0.1:8806/analysis/alarm_push'

    # 头部信息
    headers = {'Content-Type': 'application/json'}
    data = {
        "EventType":
            "alg_task_alarm_push",
        "AlarmInfo":
            {
                "Number": 1,
                "Item": [
                    {

                    }
                ]
            }
    }
    data_item = data['AlarmInfo']['Item'][0]
    for key, value in alarm_info.items():
        data_item[key] = value

    r = requests.post(url, data=json.dumps(data), headers=headers)
    print('response success')
    print(r.text)
    print(r.status_code)


if __name__ == '__main__':
    test_test = {
        "name1": 'name1',
        'name2': 'name2'
    }
    alarm_push_info(**test_test)
    # push_img('img0.jpg','./img0.jpg')
