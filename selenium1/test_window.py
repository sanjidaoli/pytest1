#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : test_window.py
@Project     : pytest1
@Time        : 2021/4/8 21:39
@Author      : LHQ
@Software    : PyCharm
"""
from time import sleep

from selenium1.Base import Base


class TestWindow(Base):
    def test_windows(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        sleep(2)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div/div/div/div/div/div[3]/p[2]").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("user")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)