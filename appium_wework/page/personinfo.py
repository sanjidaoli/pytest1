#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : personinfo.py
@Project     : pytest1
@Time        : 2021/7/25 16:40
@Author      : LHQ
@Software    : PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_wework.page.base_page import BasePage
from appium_wework.page.personinfoedit import PersonInfoEdit


class PersonInfo(BasePage):
    def edit(self):
        # 跳转到编辑成员
        self.find(MobileBy.ID,"com.tencent.wework:id/hcg").click()
        return PersonInfoEdit(self._driver)

