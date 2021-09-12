#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : member_invite.py
@Project     : pytest1
@Time        : 2021/7/18 14:43
@Author      : LHQ
@Software    : PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_wework.page.base_page import BasePage


class MemberInviteMenuActivity(BasePage):
    def addmember_by_manul(self):
        # self._driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.find(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        from appium_wework.page.add_contact import ContactAddActivity
        return ContactAddActivity(self._driver)

    def get_toast(self):
        # return self._driver.find_element_by_xpath("//*[@text='添加成功']").text
        return self.find(MobileBy.XPATH,"//*[@text='添加成功']").text
