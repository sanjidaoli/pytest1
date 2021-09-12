#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : Base.py
@Project     : pytest1
@Time        : 2021/4/8 21:42
@Author      : LHQ
@Software    : PyCharm
"""
from selenium import webdriver
class Base():
    def setup(self):
        # browser = os.getenv("browser")
        # if browser == 'firefox':
        #     self.driver = webdriver.Firefox()
        # elif browser == "headless":
        #     self.driver = webdriver.PhantomJS()
        # else:
        #     self.driver = webdriver.Chrome()

        self.driver =webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()