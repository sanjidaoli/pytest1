#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : test_frame.py
@Project     : pytest1
@Time        : 2021/4/8 22:32
@Author      : LHQ
@Software    : PyCharm
"""
from selenium1.Base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
