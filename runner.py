# _*_ coding: utf-8 _*_
# @Time     : 2022-10-31 22:00
# @Author   : Mr zhang
# @FileName : runner.py
# @Software : PyCharm
# @Blog     : https://blog.csdn.net/qq_45361084
from ip_api import run as api_run
from ip_collection import run as col_run
from ip_verify import run as ver_run
from multiprocessing import Process
import threading


def run():
    # 启动三个进程
    p1 = Process(target=api_run)
    p3 = Process(target=ver_run)

    p1.start()
    p3.start()

    # 启动一个线程执行 col_run 函数
    t = threading.Thread(target=col_run)
    t.start()

    # 等待线程结束
    t.join()


if __name__ == '__main__':
    run()
