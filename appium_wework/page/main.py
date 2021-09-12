#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : main.py
@Project     : pytest1
@Time        : 2021/7/18 14:33
@Author      : LHQ
@Software    : PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_wework.page.addresslist import AddressList
from appium_wework.page.base_page import BasePage


class Main(BasePage):
    def goto_message(self):
        pass
    def goto_addresslist(self):
        # self._driver.find_element_by_xpath("//*[@text='通讯录']").click()
        # self._driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.find(MobileBy.XPATH,"//*[@text='通讯录']").click()

        return AddressList(self._driver)

    def goto_workbench(self):
        pass
    def goto_me(self):
        pass