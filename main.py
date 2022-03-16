from flask import Flask, request, jsonify
import json
# from settings import APP_PORT
import share_data
from share_data import globalData

# 创建一个服务
app = Flask(__name__)


# 创建一个接口 指定路由和请求方法 定义处理请求的函数
@app.route(rule='/analysis/interface/', methods=['POST'])
def everything():
    # 1.获取 JSON 格式的请求体 并解析拿到数据

    # if not request.data:  # 检测是否有数据
    #     return 'fail'

    request_body = request.get_json()

    print('request.data:', request.data)

    # 把获取到的数据转为JSON格式
    share_data.globalData.request_data = json.loads(request.data.decode('utf-8'))
    print(share_data.globalData.request_data)

    event_type = share_data.globalData.request_data['EventType']

    # 2.拿到数据后，根据事件类型做出不同的响应
    response_data = ''



    task_config_flag = False
    inquire_flag = True

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
    return response_data



# 最终对请求进行相应



if __name__ == '__main__':
    # 启动服务 指定主机和端口
    app.run(host='127.0.0.1', port=8888, debug=False)
