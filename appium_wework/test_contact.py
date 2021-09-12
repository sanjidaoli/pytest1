#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : test_contact.py
@Project     : pytest1
@Time        : 2021/7/17 15:30
@Author      : LHQ
@Software    : PyCharm
"""
from time import sleep

from appium import webdriver

class TestWeiXin:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        # caps["deviceName"] = "127.0.0.1:62001"
        caps["deviceName"] = "192.168.2.102:5555"
        caps['platformVersion'] = '9'
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = "com.tencent.wework.launch.WwMainActivity"
        # caps["appPackage"] = "com.xueqiu.android"
        # caps["appActivity"] = "com.xueqiu.android.main.view.MainActivity"
        caps["noReset"] = "true"
        # caps["automationName"] = "uiautomator2"
        # caps["skipServerInitialization"] = True
        # caps["skipDeviceInitialization"] = True
        # self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        print("teardown")
        self.driver.quit()

    def test_addcontact(self):

        print("添加联系人")
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        self.driver.find_element_by_xpath("//*[@text='添加成员']").click()
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        name_element = self.driver.find_element_by_xpath("//*[@text='姓名　']/..//*[@class='android.widget.EditText']")
        name_element.send_keys("lili")
        self.driver.find_element_by_xpath("//*[@text='性别']/..//*[@class='android.widget.TextView' and @text='男' ]").click()
        self.driver.find_element_by_xpath("//*[@text='女']").click()
        mobile_element = self.driver.find_element_by_xpath("//*[@text='手机　']/..//*[@class='android.widget.EditText']")
        mobile_element.send_keys('15012345671')

        # 获得机器屏幕大小x,y
        def getSize():
            x = self.driver.get_window_size()['width']
            y = self.driver.get_window_size()['height']
            return (x, y)

        # 屏幕向上滑动
        def swipeUp(t):
            l = getSize()
            x1 = int(l[0] * 0.5)  # x坐标
            y1 = int(l[1] * 0.75)  # 起始y坐标
            y2 = int(l[1] * 0.25)  # 终点y坐标
            self.driver.swipe(x1, y1, x1, y2, t)

        # 屏幕向下滑动
        def swipeDown(t):
            l = getSize()
            x1 = int(l[0] * 0.5)  # x坐标
            y1 = int(l[1] * 0.25)  # 起始y坐标
            y2 = int(l[1] * 0.75)  # 终点y坐标
            self.driver.swipe(x1, y1, x1, y2, t)

        # 屏幕向左滑动
        def swipLeft(t):
            l = getSize()
            x1 = int(l[0] * 0.75)
            y1 = int(l[1] * 0.5)
            x2 = int(l[0] * 0.05)
            self.driver.swipe(x1, y1, x2, y1, t)

        # 屏幕向右滑动
        def swipRight(t):
            l = getSize()
            x1 = int(l[0] * 0.05)
            y1 = int(l[1] * 0.5)
            x2 = int(l[0] * 0.75)
            self.driver.swipe(x1, y1, x2, y1, t)
        swipeUp(1000)
        self.driver.find_element_by_id('com.tencent.wework:id/ad3').click()
        print(self.driver.page_source)
        self.driver.find_element_by_xpath("//*[@text='添加成功']")
