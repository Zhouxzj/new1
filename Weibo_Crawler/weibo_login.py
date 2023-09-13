from selenium import webdriver
from time import sleep
import json

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://weibo.com/login.php')
    sleep(6)
    # driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe')) # 切换浏览器标签定位的作用域
    driver.find_element('xpath', '//*[@id="pl_login_form"]/div/div[1]/div/a[2]').click()
    sleep(15)
    dictCookies = driver.get_cookies()  # 获取list的cookies
    jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存
    with open('cookies.txt', 'a+') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')
    driver.close()
    driver.quit()


def browser_initial():
    new_browser = webdriver.Chrome()
    new_browser.maximize_window()
    new_browser.get('https://weibo.com/login.php')
    return new_browser


def log_csdn(new_browser):
    with open('cookies.txt', 'r', encoding='utf8') as f:
        list_cookies = json.loads(f.read())

    # 往browser里添加cookies
    for cookie in list_cookies:
        cookie_dict = {
            'domain': '.weibo.com',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        }
        new_browser.add_cookie(cookie_dict)
    sleep(3)
    new_browser.refresh()  # 刷新网页,cookies才成功


if __name__ == "__main__":
    browser = browser_initial()
    log_csdn(browser)
