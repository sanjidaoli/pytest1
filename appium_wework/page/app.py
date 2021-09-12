#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : app.py
@Project     : pytest1
@Time        : 2021/7/18 14:30
@Author      : LHQ
@Software    : PyCharm
"""
from appium import webdriver

from appium_wework.page.base_page import BasePage
from appium_wework.page.main import Main


class App(BasePage):
    _appPackage="com.tencent.wework"
    _appActivity="com.tencent.wework.launch.WwMainActivity"
    def start(self):
        if self._driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:62001"
            caps["appPackage"] = self._appPackage
            caps["appActivity"] = self._appActivity
            caps["noReset"] = "true"
            caps["skipServerInitialization"] = True
            caps["skipDeviceInitialization"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            # self._driver.launch_app()
            self._driver.start_activity(self._driver,self._appPackage,self._appActivity)

        self._driver.implicitly_wait(5)

        return self

    def restart(self):
        pass

    def stop(self):
        self._driver.quit()
    def main(self) -> Main:
        return  Main(self._driver)