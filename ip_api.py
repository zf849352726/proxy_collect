# _*_ coding: utf-8 _*_
# @Time     : 2022-10-31 22:00
# @Author   : Mr zhang
# @FileName : ip_api.py
# @Software : PyCharm
# @Blog     : https://blog.csdn.net/qq_45361084
# 代理的IP的api接口
from proxy_redis import ProxyRedis
from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS

# 1. 创建app
app = Sanic("ip")
# 2. 解决跨域
CORS(app)

red = ProxyRedis()

# 3. 准备处理http请求的函数
@app.route("/get_proxy")  # 路由配置
def dispose(rep):
    ip_list = red.get_avail_proxy()
    return json({"ip": ip_list})  # 返回给客户端


def run():
    app.run(host="127.0.0.1", port=5800)


if __name__ == '__main__':
    run()
