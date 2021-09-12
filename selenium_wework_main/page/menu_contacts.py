#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : menu_contacts.py
@Project     : pytest1
@Time        : 2021/5/4 16:35
@Author      : LHQ
@Software    : PyCharm
"""
from time import sleep

from selenium.webdriver.common.by import By

from selenium_wework_main.page.add_member import AddMember

#企业微信通讯录
from selenium_wework_main.page.base_page import BasePage


class Menu_Contacts(BasePage):
    def goto_add_member1(self):
        # self._driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        self._driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        return AddMember(self._driver)

    def goto_add_member2(self):
        # self._driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[9]/a[1]').click()
        self._driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[9]/a[1]').click()
        return AddMember(self._driver)
    
