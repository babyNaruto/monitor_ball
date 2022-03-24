import requests
import json


# 获取设备id
def get_dev_id():
    dev_url = 'http://127.0.0.1:8807/2500/ipc/get/'
    # 头部信息
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "EventType": "get_device_id"
    }
    r = requests.post(dev_url, data=json.dumps(data), headers=headers)
    if r.status_code == 200:
        print('设备ID获取成功！')
        DeviceSno = r.text
    else:
        print('设备ID获取失败！')
        DeviceSno = ''

    print(DeviceSno)
    return DeviceSno


# 告警图片推送
def push_img(alarm_img_name, alarm_img_url):
    # 地址1:需要拿到设备Id的平台
    url_1 = "https://surveillance-api.whhyxkj.com/camera/api/violation-manage/upload/file"

    # 地址2
    url_2 = "http://127.0.0.1:8807/analysis/alarm_push/"

    files = [
        ('image', (alarm_img_name, open(alarm_img_url, 'rb'), 'image/jpeg'))
    ]
    headers = {
        "token": 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzeXN0ZW0iLCJuYW1lIjoi6L-d56ug5LiK5LygIiwidHlwZSI6IjEiLCJ1c2VySWQiOiJzeXN0ZW0iLCJpYXQiOjE2NDgwMTg4NzJ9.HilTvzEUBul2JGJq2NlbxA2OUCgglauhYHFGv6KcPnHSnCPYJK5xgSNnLoFi67W5TkBOBDgf3X_r2h0fS-eihw'
    }
    # 平台1图片推送
    response_1 = requests.request("POST", url_1, headers=headers, files=files)
    if response_1.status_code == 200:
        print('平台1图片推送成功', response_1.status_code)
        print(response_1.text)
    else:
        print('平台1图片推送失败', response_1.status_code)
        print(response_1.text)
    # 平台2图片推送
    response_2 = requests.request("POST", url_2, headers=headers, files=files)
    if response_2.status_code == 200:
        print('平台2图片推送成功', response_2.status_code)
        print(response_2.text)
    else:
        print('平台2图片推送失败', response_2.status_code)
        print(response_2.text)


# 告警信息推送

def alarm_push_info(alarm_info):
    # 地址1：需要拿到设备ID的平台
    url_1 = "https://surveillance-api.whhyxkj.com/camera/api/violation-manage/upload/violation"
    # 地址2
    url_2 = "http://127.0.0.1:8807/analysis/alarm_push/"

    # 头部信息
    headers = {
        "Content-Type": 'application/json',
        "token": 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzeXN0ZW0iLCJuYW1lIjoi6L-d56ug5LiK5LygIiwidHlwZSI6IjEiLCJ1c2VySWQiOiJzeXN0ZW0iLCJpYXQiOjE2NDgwMTg4NzJ9.HilTvzEUBul2JGJq2NlbxA2OUCgglauhYHFGv6KcPnHSnCPYJK5xgSNnLoFi67W5TkBOBDgf3X_r2h0fS-eihw'
    }
    data_1 = {
        "EventType":
            "alg_task_alarm_push",
        "AlarmInfo":
            {
                "Number": 1,
                "Item": alarm_info
            }
    }

    # 平台2推送
    r_2 = requests.request("POST", url_2, data=json.dumps(data_1), headers=headers)
    if r_2.status_code == 200:
        print('平台2信息推送成功', r_2.status_code)
        print(r_2.text)
    else:
        print('平台2信息推送失败', r_2.status_code)
        print(r_2.text)

    # 平台1推送,多加推送数据设备
    # 得到设备ID
    device_id = json.loads(get_dev_id())['DeviceSno']
    data_2 = data_1
    data_2['AlarmInfo']['Item'][0]['DeviceSno'] = device_id
    r_1 = requests.post(url_1, data=json.dumps(data_2), headers=headers)

    if r_1.status_code == 200:
        print('平台1信息推送成功', r_1.status_code)
        print(r_1.text)
    else:
        print('平台1信息推送失败', r_1.status_code)


if __name__ == '__main__':
    test_test = [
        {
            "AlgCode": 1001,
            "TaskId": "AlgTask123",
            "AlarmTime": "2022-03-24 12:03:00",
            "Desc": "作业现场吸烟",
            "PictureName": "281230.jpg",
            "Type": 0,
            "Width": 1080,
            "Height": 720,
            "Size": 180309,
        }
    ]
    alarm_push_info(test_test)
    push_img('281230.jpg', './281230.jpg')
