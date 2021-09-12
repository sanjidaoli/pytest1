#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : index.py
@Project     : pytest1
@Time        : 2021/5/1 17:35
@Author      : LHQ
@Software    : PyCharm
"""
from selenium import webdriver

from selenium_wework_login.login import Login
from selenium_wework_login.register import Register


class Index:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get('https://work.weixin.qq.com/')
        self._driver.maximize_window()

    def  goto_login(self):
        #click login
        self._driver.find_element_by_css_selector('.index_top_operation_loginBtn').click()
        return Login(self._driver)
    def goto_register(self):
        #click Register
        self._driver.find_element_by_css_selector('.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)
    def quit(self):
        self._driver.quit()
