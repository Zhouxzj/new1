import json
import re
import time

import pandas as pd
from selenium import webdriver
import requests
from configparser import ConfigParser


url = "https://weibo.com/ajax/statuses/mymblog"
target = ConfigParser()
target.read('password.ini', encoding="utf-8")
phone_number = target.get('weibo', 'phone_number')
pwd = target.get('weibo', 'password')
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.set_window_size(1200, 1000)
driver.get(r'https://weibo.com/login.php/')
driver.find_element("id", "loginname").send_keys(phone_number)
driver.find_element("xpath", "//div[@class='info_list password']/div/input").send_keys(pwd)
driver.find_element("xpath", "//div[@class='info_list login_btn']/a").click()
# driver.find_element("id", "dmCheck").click()
# 短信验证码登录
driver.find_element("id", "messageCheck").click()
driver.find_element("id", "message_sms_login").click()
check_code = input("输入验证码：")
time.sleep(20)
for i in range(0, 6):
    driver.find_element("xpath", '//div[@class="num clearfix"]/input[{}]'.format(i + 1)).send_keys(check_code[i])
# # 发送私信登录
# # driver.find_element("id", 'send_dm_btn').click()
time.sleep(20)
# got_cookies = driver.get_cookies()
# format_cookie = ''.join([f'{i["name"]}={i["value"]}; ' for i in got_cookies])[:-2]
# print(type(format_cookie))
# print(format_cookie)


# 获取cookies 到本地
def get_cookies(driver_new):
    driver_new.get('https://weibo.com/login.php')
    time.sleep(20)  # 留时间进行扫码
    cookies = driver.get_cookies()  # 获取list的cookies
    js_cookies = json.dumps(cookies)  # 转换成字符串保存
    with open('cookies.txt', 'w') as f:
        f.write(js_cookies)
    print('cookies已重新写入！')


# 读取本地的cookies
def read_cookies():
    with open('cookies.txt', 'r', encoding='utf8') as f:
        cookies = json.loads(f.read())
    cookies = []
    for cookie in cookies:
        cookie_dict = {
            'domain': '.weibo.com',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            'expires': '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        }
        cookies.append(cookie_dict)
    return cookies


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36',
    "Cookie": "SINAGLOBAL=7042556481415.465.1689255052862; UOR=,,www.baidu.com; "
              "ULV=1691716667261:9:1:1:8782116420855.546.1691716667259:1690613644978; "
              "XSRF-TOKEN=4AIrsjZx7FGSNNul1Y4JvsgK; "
              "SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whir5I_Xeyi.9v4OCLYp9Ka5JpX5KMhUgL"
              ".FoMRSoz71hn7e0z2dJLoI0qLxKnLBKMLBKqLxKBLBonL12BLxK-L1hnLBo5LxKML1-2L1hBLxK-L12eL1KMLxKqL1KqLBo.t; "
              "ALF=1694436027; SSOLoginState=1691844028; "
              "SCF=Ar4w_JsP-G65GX_moI4Z1yMAIHO1Ue96zlQTCQVwr1uTbza4xRb6M89VdjsMSF5q4NtrWiLCXiHJFmc9dIJujM8.; "
              "SUB=_2A25J0w3tDeRhGeFG7VAR-CbMyD6IHXVqqXglrDV8PUNbmtAbLUv1kW9NeT7-Z36301GVQBRWlBn39ozONTL3pnm9; "
              "WBPSESS=eQZNrz-Wn46RlA5U6QxZXwXIRRcmw4oxdQQApLATMm-kSeyQ9z8xdFuCM2a8zshoBbNwM4qXrwkAY1C6s"
              "-DMwr4rG61EymqxUeqlMBmk8Z-xsg9eIAx0n_V4lgnN0Jkxsglv5umNwJyHyjHe_I70Kg==; ariaDefaultTheme=undefined",
    "Accept": "application/json, text/plain, */*"
}


# def shanghai_subway_crawl(num):
#     params = {
#         "uid": 1742987497,
#         "page": num,
#         "feature": 0,
#     }
#     response = requests.get(url, headers=headers, params=params)
#     # response.encoding = "gb2312
#     print(response.status_code, num)
#     content = json.loads(response.text)
#     data = content["data"]
#     items = data["list"]
#     results = []
#     for item in items:
#         text = item["text_raw"]
#         # print(text)
#         # 【地铁网络客流】7月24日上海地铁总客流为1205.0万人次。 ​
#         if re.match(r"【地铁网络客流】\d月.+日上海地铁总客流为\d+.\d万人次。", text):
#             month = "".join(re.findall(r"【地铁网络客流】(.+?)月", text))
#             day = "".join(re.findall(r"月(.+?)日", text))
#             number = "".join(re.findall(r"为(.+?)万人次", text))
#             results.append({
#                 "月份": month,
#                 "日期": day,
#                 "总客流/万人次": number,
#                 "综述": text
#             })
#     return results
#
#
# outcomes = []
# for x in range(1, 70):
#     outcomes.extend(shanghai_subway_crawl(x))
#
#
# df = pd.DataFrame(outcomes)
# df.to_excel("./地铁客流数据.xlsx")
