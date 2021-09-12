#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : 123.py
@Project     : pytest1
@Time        : 2021/5/16 16:03
@Author      : LHQ
@Software    : PyCharm
"""
from appium import webdriver
dessired_cap ={}
dessired_cap['platformName']='Android'
dessired_cap['platformVersion']='6.0'
dessired_cap['deviceName']='emulator-5554'
dessired_cap['appPackage']='com.android.settings'
dessired_cap['appActivity']='com.android.settings.Settings'
driver = webdriver.Remote("http://localhost:4723/wd/hub",dessired_cap)
driver.quit()



