#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : test_register.py
@Project     : pytest1
@Time        : 2021/5/1 18:58
@Author      : LHQ
@Software    : PyCharm
"""
from time import sleep

from selenium_wework_login.index import Index


class TestRegiter:
    def setup(self):
        self.index = Index()
    def test_register(self):
        # self.index.goto_login().goto_register().register()
        self.index.goto_register().register()
    def teardown(self):
        sleep(5)
        self.index.quit()