#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : add_contact.py
@Project     : pytest1
@Time        : 2021/7/18 14:45
@Author      : LHQ
@Software    : PyCharm
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from appium_wework.page.base_page import BasePage
from appium_wework.page.move_screen import MoveScreen


class ContactAddActivity(BasePage):
    def input_name(self,name):
        name_element = self.find(MobileBy.XPATH,"//*[@text='姓名　']/..//*[@class='android.widget.EditText']")
        name_element.send_keys(name)
        return self
    def set_gender(self):
        self.find(MobileBy.XPATH,"//*[@text='性别']/..//*[@class='android.widget.TextView' and @text='男' ]").click()
        self.find(MobileBy.XPATH,"//*[@text='女']").click()
        return self
    def input_phonenum(self,telno):
        mobile_element = self.find(MobileBy.XPATH,"//*[@text='手机　']/..//*[@class='android.widget.EditText']")
        mobile_element.send_keys(telno)
        return self
    def move_up(self):
        def getSize():
            x = self._driver.get_window_size()['width']
            y = self._driver.get_window_size()['height']
            return (x, y)

        def swipeUp(t):
            l = getSize()
            x1 = int(l[0] * 0.5)  # x坐标
            y1 = int(l[1] * 0.75)  # 起始y坐标
            y2 = int(l[1] * 0.25)  # 终点y坐标
            self._driver.swipe(x1, y1, x1, y2, t)
        swipeUp(10000)
        return self

    def click_save(self):
        from appium_wework.page.member_invite import MemberInviteMenuActivity
        self._driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("保存"))').click()
        # self.find(MobileBy.ID,'com.tencent.wework:id/ad3').click()
        return MemberInviteMenuActivity(self._driver)
    def del_member(self):
        sleep(3)
        self._driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("删除成员"))').click()
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        # self.find(MobileBy.ID,"com.tencent.wework:id/e6a").click()
        # self.find(MobileBy.ID,"com.tencent.wework:id/bga").click()
        from appium_wework.page.addresslist import AddressList
        return AddressList(self._driver)