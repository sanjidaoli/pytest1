#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : miui.py
@Project     : pytest1
@Time        : 2021/7/18 18:53
@Author      : LHQ
@Software    : PyCharm
"""
#coding=utf-8
from appium import webdriver
from time import sleep
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = '41472661'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.MiuiSettings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(1)
driver.swipe(200,1000,200,10,800)
sleep(1)
driver.swipe(200,1000,200,10,800)
sleep(1)
driver.swipe(200,1000,200,10,800)
sleep(1)
driver.tap([(596,391)])
sleep(1)
driver.tap([(539,481)])
sleep(1)
driver.tap([(431,374)])
sleep(1)
driver.tap([(540,584)])
sleep(1)
driver.tap([(798,1817)])
