import requests
import os
import json
import shareData
import server

device_id = {"Ipc_code": 0}


# 获取设备id
def get_dev_id():
    dev_url = 'http://127.0.0.1:8807/2500/ipc/get/'
    # 头部信息
    headers = {'Content-Type': 'application/json'}
    data = {
        "EventType": "get_device_id"
    }
    r = requests.post(dev_url, data=json.dumps(data), headers=headers)
    device_id = r.text
    print(r.text, device_id)
    return device_id


# 告警图片推送
def push_img(alarm_img_name, alarm_img_url):
    # 地址1
    url_1 = "http://127.0.0.1:8807/analysis/alarm_push/"
    # 地址2
    url_2 = "http://127.0.0.1:8808/analysis/alarm_push/"

    payload = {}

    files = [
        ('image', (alarm_img_name, open(alarm_img_url, 'rb'), 'image/jpeg'))
    ]
    headers = {
        'Content-Type': 'image/jpeg',
    }

    response_1 = requests.request("POST", url_1, headers=headers, data=payload, files=files)
    response_2 = requests.request("POST", url_2, headers=headers, data=payload, files=files)
    # 平台1
    print('平台1', response_1.status_code)
    print('response_1 success')
    print(response_1.text)
    # 平台2
    print('平台2', response_2.status_code)
    print('response_2 success')
    print(response_2.text)


# 告警信息推送

def alarm_push_info(**alarm_info):
    # 地址1
    url_1 = "http://127.0.0.1:8807/analysis/alarm_push/"
    # 地址2
    url_2 = "http://127.0.0.1:8808/analysis/alarm_push/"

    # 头部信息
    headers = {'Content-Type': 'application/json'}
    data_1 = {
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

    data_item = data_1['AlarmInfo']['Item'][0]
    for key, value in alarm_info.items():
        data_item[key] = value

    # 平台1推送

    r_1 = requests.post(url_1, data=json.dumps(data_1), headers=headers)
    if r_1.status_code == 200:
        print('r_1 success', r_1.status_code)
        print(r_1.text)
    else:
        print('r_1 fail', r_1.status_code)

    # 平台2推送,多加数据Ipc_code
    device_id = json.loads(get_dev_id())

    data_2 = data_1
    data_2['Ipc_code'] = device_id['Ipc_code']
    r_2 = requests.post(url_2, data=json.dumps(data_2), headers=headers)

    if r_2.status_code == 200:
        print('r_2 success', r_2.status_code)
        print(r_2.text)
    else:
        print('r_2 fail', r_2.status_code)


if __name__ == '__main__':
    test_test = {
        "name1": 'name1',
        'name2': 'name2'
    }
    # 传入alg_task_alarm_push Item[]里面的字典数据
    # get_dev_id()
    alarm_push_info(**test_test)
    # push_img('img0.jpg','./img0.jpg')
