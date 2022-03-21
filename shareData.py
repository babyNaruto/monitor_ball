class GlobalResult:
    # 1.获取设备算法能力响应数据
    ability_res = {
        "EventType": "alg_ability_request",
        "Result":
            {
                "Code": 200,
                "Desc": ""
            },
        "AbilityInfo":
            {
                "Number": 2,
                "Ability":
                    [
                        {
                            "AlgCode": 1001,
                            "CodeDesc": ""
                        },
                        {
                            "AlgCode": 1002,
                            "CodeDesc": ""
                        }
                    ]
            }
    }

    # 2.算法任务配置响应数据
    task_config_res = {
        "EventType": "alg_task_config",
        "TaskId": "AlgTask123",
        "Result": {
            "Code": 200,
            "Desc": ""
        }
    }

    # 3.算法任务查询响应数据
    task_request_res = {
        "EventType": "alg_task_request",
        "Result": {
            "Code": 200,
            "Desc": ""
        },
        "TaskNumber": 1,
        "Task": [
            {
                "TaskId": "AlgTask123",
                "AlgCode": 1001,
                "TaskStatus": 1
            }
        ]
    }




class GlobalRequest:
    # #2. 对方算法
    # task_config_req = {
    #     "EventType": "alg_task_config",
    #     "TaskId": "AlgTask123",
    #     "DevCode": "123456789012345678",
    #     "Command": 1,
    #     "AlgCode": 1001,
    #     "AlarmInterval": 5,
    #     "AlarmPushUrl": "http://192.168.1.200:3400/analysis/alarm_push"
    # }
    #4.告警信息推送
    task_alarm_push = {
        "EventType":
            "alg_task_alarm_push",
        "AlarmInfo":
            {
                "Number": 1,
                "Item": [
                    {
                        "AlgCode": 1001,
                        "TaskId": "AlgTask123",
                        "AlarmTime": "2020-01-01 12:00:00",
                        "Desc": "description...",
                        "PictureName": "xxx.jpg",
                        "Type": 0,
                        "Width": 1080,
                        "Height": 720,
                        "Size": 180309
                    }
                ]
            }
    }
    device_id = {}



