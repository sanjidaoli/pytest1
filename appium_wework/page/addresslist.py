#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : addresslist.py
@Project     : pytest1
@Time        : 2021/7/18 14:39
@Author      : LHQ
@Software    : PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_wework.page.base_page import BasePage
from appium_wework.page.member_invite import MemberInviteMenuActivity


class AddressList(BasePage):
    def add_member(self):
        # self._driver.find_element_by_xpath("//*[@text='添加成员']").click()
        self.find(MobileBy.XPATH,"//*[@text='添加成员']").click()
        return MemberInviteMenuActivity(self._driver)
    def del_member(self,name):
        self.find(MobileBy.XPATH,"//*[@class='android.widget.TextView' and @text='"+name+"']").click()
        from appium_wework.page.personinfo import PersonInfo
        return PersonInfo(self._driver)