#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : personinfoedit.py
@Project     : pytest1
@Time        : 2021/7/25 16:44
@Author      : LHQ
@Software    : PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_wework.page.base_page import BasePage


class PersonInfoEdit(BasePage):
    def edit_member(self):
        # 点击编辑成员
        self.find(MobileBy.ID,"com.tencent.wework:id/b5t").click()
        from appium_wework.page.add_contact import ContactAddActivity
        return ContactAddActivity(self._driver)