# _*_ coding: utf-8 _*_
# @Time     : 2022-10-31 21:54
# @Author   : Mr zhang
# @FileName : ip_collection.py
# @Software : PyCharm
# @Blog     : https://blog.csdn.net/qq_45361084
# 代理IP的采集
from proxy_redis import ProxyRedis
import requests
from lxml import etree
import time
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By




headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}

# 采集快代理
def get_kuai_ip(red):
        url = "https://www.kuaidaili.com/free/intr/1/"
        resp = requests.get(url, headers=headers)
        tree = etree.HTML(resp.text)
        trs = tree.xpath("//table/tbody/tr")
        for tr in trs:
            ip = tr.xpath("./td[1]/text()")  # ip地址
            port = tr.xpath("./td[2]/text()")  # 端口
            if not ip:
                continue
            ip = ip[0]
            port = port[0]
            proxy_ip = ip + ":" + port

            red.add_proxy_ip(proxy_ip)  # 增加ip地址


# 采集66免费代理网
def get_66_ip(red):
    url = "http://www.66ip.cn/areaindex_1/1.html"
    resp = requests.get(url, headers=headers)
    tree = etree.HTML(resp.text)
    trs = tree.xpath("//table//tr")[1:]
    for tr in trs:
        ip = tr.xpath("./td[1]/text()")  # ip地址
        port = tr.xpath("./td[2]/text()")  # 端口
        if not ip:
            continue
        ip = ip[0]
        port = port[0]
        proxy_ip = ip + ":" + port

        red.add_proxy_ip(proxy_ip)  # 增加ip地址

# 采集高可用全球免费代理IP库
def get_quan_ip(red):
    url = "https://ip.jiangxianli.com/?page=1"
    resp = requests.get(url, headers=headers)
    tree = etree.HTML(resp.text)
    trs = tree.xpath("//table//tr")
    for tr in trs:
        ip = tr.xpath("./td[1]/text()")  # ip地址
        port = tr.xpath("./td[2]/text()")  # 端口
        if not ip:
            continue
        ip = ip[0]
        port = port[0]
        proxy_ip = ip + ":" + port

        red.add_proxy_ip(proxy_ip)  # 增加ip地址

# 爬取支持conn ssl post的ip https://freeproxylist.org/en/free-proxy-list.htm?index=2


def get_free_ip(red):
    options = Options()

    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Referer': 'https://freeproxylist.org',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    }
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument(f'user-agent={headers["User-Agent"]}')
    options.add_argument(f'referer={headers["Referer"]}')
    options.add_argument(f'accept-language={headers["Accept-Language"]}')

    options.add_experimental_option('detach', True)

    url = 'https://freeproxylist.org/en/free-proxy-list.htm'
    # 自动下载和配置 ChromeDriver
    driver_path = ChromeDriverManager().install()

    # 创建 Service 对象，传入 ChromeDriver 的路径
    service = Service(driver_path)

    # 创建 Chrome 对象时，传入 service 和 options 对象
    driver = Chrome(service=service, options=options)
    driver.get(url)

    # 筛选条件
    # 找到下拉框元素
    select_elem_free = driver.find_element(By.ID, 'select9')

    # 创建 Select 对象
    select = Select(select_elem_free)

    # 通过文本内容选择选项
    select.select_by_visible_text('free proxy servers')

    # 找到下拉框元素
    select_elem_https = driver.find_element(By.ID, 'select2')


    # 创建 Select 对象
    select = Select(select_elem_https)

    # 通过文本内容选择选项
    select.select_by_visible_text('yes')

    # 找到下拉框元素
    select_elem_coon = driver.find_element(By.ID, 'select4')


    # 创建 Select 对象
    select = Select(select_elem_coon)

    # 通过文本内容选择选项
    select.select_by_visible_text('yes')

    # 找到下拉框元素
    select_elem_post = driver.find_element(By.ID, 'select8')


    # 创建 Select 对象
    select = Select(select_elem_post)

    # 通过文本内容选择选项
    select.select_by_visible_text('yes')

    # url = 'https://freeproxylist.org/en/captcha.jpg'
    # filename = 'image.jpg'
    #
    # urllib.request.urlretrieve(url, filename)
    # # 识别验证码或手输入

    code = input("请手动输入验证码")

    # 找到验证码文本框
    code_input = driver.find_element(By.XPATH, '//*[@id="code"]')
    code_input.send_keys(code)

    # 提交筛选
    submit_tag = driver.find_element(By.XPATH, '// *[@id="filter"]')
    submit_tag.click()

    trs = driver.find_elements(By.XPATH, '//*[@id="proxytable"]/tbody/tr')
    # print(trs)
    for i, tr in enumerate(trs):
        proxy_ip = tr.find_elements(By.XPATH, './/td')[1].text  # ip地址+端口
        # print(ip)
        if not proxy_ip:
            continue
        red.add_proxy_ip(proxy_ip)  # 增加ip地址
    time.sleep(10)
    driver.quit()

def run():
    red = ProxyRedis()  # 创建redis存储
    while True:
        try:
            # get_kuai_ip(red)  # 采集快代理
            # get_66_ip(red)  # 采集66免费代理
            # get_quan_ip(red)  # 采集全球免费ip代理库
            get_free_ip(red)
        except:
            print("出错了")
        time.sleep(60)  # 每分钟跑一次


if __name__ == '__main__':
    run()
