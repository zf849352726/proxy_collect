# _*_ coding: utf-8 _*_
# @Time     : 2022-10-31 22:39
# @Author   : Mr zhang
# @FileName : if_use.py
# @Software : PyCharm
# @Blog     : https://blog.csdn.net/qq_45361084
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}


def get_proxy():
    url = "http://127.0.0.1:5800/get_proxy"
    resp = requests.get(url, headers=headers)
    ips = resp.json()
    for ip in ips["ip"][0]:
        yield ip  # 生成器


def spider():
    url = "http://www.baidu.com/"
    while True:
        try:
            proxy_ip = next(gen)
            proxy = {
                "http:": "http:" + proxy_ip,
                "https:": "http:" + proxy_ip
            }
            resp = requests.get(url, proxies=proxy, headers=headers)
            resp.encoding = "utf-8"
            return resp.text
        except:
            print("代理失效了")


if __name__ == '__main__':
    gen = get_proxy()
    page_source = spider()
    print(page_source)
