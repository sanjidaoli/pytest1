#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : TestForm.py
@Project     : pytest1
@Time        : 2021/4/4 16:21
@Author      : LHQ
@Software    : PyCharm
"""
from time import sleep

from selenium import webdriver


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("123")
        self.driver.find_element_by_id("user_password").send_keys("password")
        # self.driver.find_element_by_id("user_remember_me").click()
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[3]/div/label').click()
        # self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        sleep(5)