#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : test_js.py
@Project     : pytest1
@Time        : 2021/4/10 15:00
@Author      : LHQ
@Software    : PyCharm
"""
import pytest

from selenium1.Base import Base
from selenium import webdriver
import time

class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("测试")
        element = self.driver.execute_script('return document.getElementById("su")')
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/a[1]/span[2]').click()
        time.sleep(3)
        for code in [
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))
    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script(
            'a=document.getElementById("train_date");a.removeAttribute("readonly");')
        self.driver.execute_script('document.getElementById("train_date").value="2020-12-30"')
        time.sleep(3)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))