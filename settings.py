# _*_ coding: utf-8 _*_
# @Time     : 2022-10-31 21:57
# @Author   : Mr zhang
# @FileName : settings.py
# @Software : PyCharm
# @Blog     : https://blog.csdn.net/qq_45361084
# 配置文件

# proxy_redis
# redis主机ip地址
REDIS_HOST = "127.0.0.1"
# redis端口号
REDIS_PORT = 6379
# redis数据库编号
REDIS_DB = 2
# redis的密码
REDIS_PASSWORD = "123456"

# redis的key
REDIS_KEY = "proxy_ip"

# 默认的ip分值
DEFAULT_SCORE = 50
# 满分
MAX_SCORE = 100

# ip_verify
# 一次检测ip的数量
SEM_COUNT = 30

