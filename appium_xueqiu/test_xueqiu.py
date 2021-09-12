#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : test_xueqiu.py
@Project     : pytest1
@Time        : 2021/8/28 15:08
@Author      : LHQ
@Software    : PyCharm
"""
from appium import webdriver
from selenium.webdriver.common.by import By

# 获取雪球页面性能参数chromedriver版本使用2.20
def test_xueqiu():
    caps = {}
    caps["platformName"] = "Android"
    caps["deviceName"] = "127.0.0.1:62001"
    caps["appPackage"] = "com.xueqiu.android"
    caps["appActivity"] = ".view.WelcomeActivityAlias"
    caps['noReset'] = "true"
    caps['chromedriverExecutable']="D:/python/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe"
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, "//*[@text='交易']").click()
    webview = driver.contexts[-1]
    driver.switch_to.context(webview)
    performance = driver.execute_script("return window.performance.timing")
    print(performance['domComplete'] - performance['responseStart'])
