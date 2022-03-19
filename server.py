from flask import Flask, request, jsonify
import json
# from settings import APP_PORT
from share_data import GlobalResult, GlobalRequest

# 创建一个服务
app = Flask(__name__)


# 创建一个接口 指定路由和请求方法 定义处理请求的函数
@app.route(rule='/analysis/interface/', methods=['POST'])
def everything():
    # 1.获取 JSON 格式的请求体 并解析拿到数据

    # request_body = request.get_json()

    print('request.data:', request.data)

    # 把获取到的数据转为字典
    request_data = json.loads(request.data.decode('utf-8'))
    print(request_data)

    event_type = request_data['EventType']

    # 2.拿到数据后，根据事件类型做出不同的响应
    response_data = ''

    # --设备算法能力查询状态--默认false
    inquire_flag = True

    # --算法任务配置状态--默认false
    task_config_flag = False

    # --算法任务查询状态--默认false
    task_request_flag = False

    # 2.1 设备算法能力查询
    if event_type == 'alg_ability_request':

        # 正在查询...

        # 查询结果字典 -> GlobalResult.ability_res

        if inquire_flag:

            # 查询成功
            print(event_type, '查询成功')
            # 生成响应信息

            # 将响应信息转换为 JSON 格式
            response_data = GlobalResult.ability_res
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
            # 生成响应信息
            response_data = inquire_fail_data

    # 2.2 算法任务配置
    elif event_type == 'alg_task_config':
        # 算法任务配置
        # 根据request_data字典的数据进行配置

        # 正在配置...

        # 配置结果 -> task_config_res

        if task_config_flag:
            # 配置成功
            print('alg_task_config success')

            response_data = GlobalResult.task_config_res
        else:
            # 配置失败
            print('alg_task_config fail')

            response_data = GlobalResult.task_config_res
    # 2.3 算法任务配置
    elif event_type == 'alg_task_request':
        # 算法任务查询

        # 正在查询...

        # 查询结果 -> GlobalResult.task_request_res

        if task_config_flag:
            # 查询成功
            print('alg_task_request success')
            response_data = GlobalResult.task_request_res
        else:
            # 查询失败
            print('alg_task_config fail')
            alg_task_request_data = {
                "EventType": "alg_ability_request",
                "Result":
                    {
                        "Code": 400,
                        "Desc": ""
                    }
            }

            response_data = alg_task_request_data

    # 最终对请求进行相应
    return response_data


if __name__ == '__main__':
    # 启动服务 指定主机和端口
    app.run(host='127.0.0.1', port=8888, debug=False)
