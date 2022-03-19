from flask import Flask, request, jsonify
import json
# from gevent import pywsgi

# from settings import APP_PORT
import share_data


# 创建一个服务
app = Flask(__name__)


# 创建一个接口 指定路由和请求方法 定义处理请求的函数
@app.route(rule='/analysis/alarm_push/', methods=['POST'])
def everything():
    # 1.获取 JSON 格式的请求体 并解析拿到数据

    # if not request.data:  # 检测是否有数据
    #     return 'fail'

    # request_body = request.get_json()
    # print('request_body:', request_body)
    print('request.data:', request.data)
    return request.data






if __name__ == '__main__':
    # 启动服务 指定主机和端口
    # server = pywsgi.WSGIServer(('127.0.0.1', 8889), app)
    app.run(host='127.0.0.1', port=8806, debug=False)

