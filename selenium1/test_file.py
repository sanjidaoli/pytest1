#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : test_file.py
@Project     : pytest1
@Time        : 2021/4/10 22:47
@Author      : LHQ
@Software    : PyCharm
"""
import time

from selenium1.Base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id("stfile").send_keys("D:/study/studypy/pytest1/selenium1/baidu.png")
        time.sleep(3)
