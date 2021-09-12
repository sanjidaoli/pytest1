#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : register.py
@Project     : pytest1
@Time        : 2021/5/1 17:40
@Author      : LHQ
@Software    : PyCharm
"""
from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self,driver:WebDriver):
        self._driver = driver

    def register(self):
        #send content
        #click element
        sleep(5)
        self._driver.find_element_by_id('corp_name').send_keys("hello1")
        self._driver.find_element_by_id('manager_name').send_keys("hello2")
        return  True