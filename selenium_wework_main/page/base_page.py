#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : base_page.py
@Project     : pytest1
@Time        : 2021/5/4 17:07
@Author      : LHQ
@Software    : PyCharm
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self,by,locator):
        self._driver.find_element(by,locator)

    def waif_for_click(self,locator,time = 10):
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))

