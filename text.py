if event_type == 'alg_ability_request':

    # 开始查询
    # 默认false

    if inquire_flag:

        # 查询成功
        print(event_type, '查询成功')
        # 生成响应信息
        # 将响应信息转换为 JSON 格式
        response_data = share_data.globalData.result_data
    else:
        # 查询失败
        print(event_type, '查询失败')
        inquire_fail_data = {
            "EventType": "alg_ability_request",
            "Result":
                {
                    "Code": 400,
                    "Desc": ""
                }
        }
        response_data = inquire_fail_data
        # 生成响应信息

# 最终对请求进行相应

elif event_type == 'alg_task_config':
    # 算法任务配置

    # 正在配置
    if task_config_flag:
        # 配置成功
        print('alg_task_config success')
        response_data = share_data.globalData.result_data
    else:
        # 配置失败
        print('alg_task_config fail')
        alg_task_data = {
            "EventType": "alg_ability_request",
            "Result":
                {
                    "Code": 400,
                    "Desc": ""
                }
        }

        response_data = alg_task_data