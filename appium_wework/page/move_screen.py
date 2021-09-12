#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : move_screen.py
@Project     : pytest1
@Time        : 2021/7/18 15:24
@Author      : LHQ
@Software    : PyCharm
"""
from appium_wework.page.base_page import BasePage


class MoveScreen(BasePage):
    def getSize(self):
        x = self._driver.get_window_size()['width']
        y = self._driver.get_window_size()['height']
        return (x, y)


    # 屏幕向上滑动
    def swipeUp(self,t):
        l = getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self._driver.swipe(x1, y1, x1, y2, t)


    # 屏幕向下滑动
    def swipeDown(t):
        l = getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self._driver.swipe(x1, y1, x1, y2, t)


    # 屏幕向左滑动
    def swipLeft(t):
        l = getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        self._driver.swipe(x1, y1, x2, y1, t)


    # 屏幕向右滑动
    def swipRight(t):
        l = getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self._driver.swipe(x1, y1, x2, y1, t)