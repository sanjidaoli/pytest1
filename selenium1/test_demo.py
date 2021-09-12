#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : test_demo.py
@Project     : pytest1
@Time        : 2021/4/11 16:12
@Author      : LHQ
@Software    : PyCharm
"""
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 将chorme浏览器添加到环境变量Path C:\Users\lhq\AppData\Local\Google\Chrome\Application
# cmd执行chrome --remote-debugging-port=9222
class TestDemo():
    def setup_method(self, method):
        # 设置options用于每次运行不会关闭浏览器
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.var = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        # self.driver.get("https://ceshiren.com/")
        # self.driver.find_element_by_xpath('//*[@id="ember27"]/a').click()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # self.driver.find_element_by_id('menu_contacts').click()
        # print(self.driver.get_cookies())
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
        #      'value': ''},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688850387805123'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'C39-AYcEnEx-dtA64TRT0d_v42kq3qwpCvzcotRPagj85qT-2P7EG6bqX7xGWrTjoK059h4FQZBzPcXaE-UApwzRmkNYVs5czEq4dvU5EvLy23xxMz6O4hSU_YHlswqjTg-wwx5KpJdymPL0JNs5P1qTmZkTU7PGlg1a4FyXwsj6Gic-I4dWTOlsu91xdwvJ1yeO9OKUY4GZBp_KEXCYtrjgXoLNuUPYwMNCh7dMTHngJwXDjiyX4BUwFwbjuLL01CFhhEwqpUnwjkZLJ6S3LQ'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688850387805123'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970324981445403'}, {'domain': '.work.weixin.qq.com', 'expiry': 1651327367, 'httpOnly': False,
        #                                     'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/',
        #                                     'secure': False, 'value': '1619790253,1619790514,1619791368'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a7192484'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'n87RD6wh4swEpi7GFva940wmj8YsOxOx0EbblJM8ClBlelZ9392Au5SmR5DDX4P9'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
        #      'path': '/', 'secure': False, 'value': '1619791368'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '383211109127651'},
        #     {'domain': '.qq.com', 'expiry': 1619877779, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.1416242219.1619790253'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1619821761, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '8hrmi8g'},
        #     {'domain': '.qq.com', 'expiry': 1682863379, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.457364353.1619790253'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1651326225, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1622383798, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'}]
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        db = shelve.open("cookies")
        # db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:
        #     # if "expiry" in cookie
        #     #     cookie.pop("expiry")
        #     # print(cookie)
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        sleep(5)
        db.close()
