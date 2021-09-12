#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : login.py
@Project     : pytest1
@Time        : 2021/5/1 17:38
@Author      : LHQ
@Software    : PyCharm
"""
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework_login.register import Register


class Login:
    def __init__(self,driver:WebDriver):
        self._driver =driver
    def scanf(self):
        pass
    def goto_register(self):
        #click register
        self._driver.find_element_by_css_selector('.login_registerBar_link').click()
        return Register(self._driver)
