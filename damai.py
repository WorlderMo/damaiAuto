"""
基于python和selenium实现的大麦网自动刷新抢票脚本
用户要提前添加好个人信息和收货地址
"""

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# 设置抢票链接和开票时间
URL = "https://piao.damai.cn/138382.html?spm=a2o6e.search.0.0.2b5328df7CB40F"
HOUR = 11
MIN  = 18

driver = webdriver.Chrome()
# 设置等待时间
wait = WebDriverWait(driver, 5)
# 以周杰伦的为例
driver.get(URL)

# test
# driver.get("https://piao.damai.cn/141699.html?spm=a2o6e.search.0.0.10f94d15pF81cd")


def choose(seletor):
    try:
        # 控件可点击时才选定
        choice = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, seletor)))
        return choice
    except TimeoutException as e:
        print("Time out!")
        return None
    except Exception:
        print("Not found!")
        return None

# 点击登录
login = choose("#userLoginInfo > span > a:nth-child(1)")
login.click()
username = choose("#login_email")
username.send_keys("13112390306")
"""
由于密码框控件被设置为不可见
先自行输入密码并记住密码
方便刷新
（也可用cookie实现）
"""

# 10秒等待用户输入密码后再开始刷
time.sleep(10)

while 1:
    if HOUR == time.localtime().tm_hour:
        while 1:
            if MIN == time.localtime().tm_min:
                print("开始抢票")
                driver.get(URL)
                price = None
                plus = None
                buybtn = None
                submit = None
                # 点击价格
                while None == price:
                    # 这里选的是580票面的，如果选其他票面，修改对应的选择器内容即可
                    price = choose("li.itm-oos:nth-child(2)")
                print(price)
                price.click()
                # 数量加1
                while None == plus:
                    plus = choose("a.btn:nth-child(3)")
                plus.click()
                # 立即抢购
                while None == buybtn:
                    buybtn = choose("#btnBuyNow")
                buybtn.click()
                # 提交订单
                while None == submit:
                    submit = choose("#orderConfirmSubmit")
                submit.click()
                break
   
time.sleep(10)
# driver.quit()
price("抢票成功")
