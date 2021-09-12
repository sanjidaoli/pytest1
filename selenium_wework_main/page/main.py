#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : main.py
@Project     : pytest1
@Time        : 2021/5/1 21:55
@Author      : LHQ
@Software    : PyCharm
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base_page import BasePage
from selenium_wework_main.page.menu_contacts import Menu_Contacts

#企业微信首页

class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_add_member(self):
        # click add member
        # self._driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        locator = (By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)')
        # WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.waif_for_click(locator)
        self._driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        # self._driver.find_element_by_css_selector('.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMember(self._driver)
    def goto_menu_contacts(self):
        locator1 = (By.ID, 'menu_contacts')
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator1))
        self._driver.find_element(By.ID,'menu_contacts').click()
        # self._driver.find_element_by_id('menu_contacts').click()
        return Menu_Contacts(self._driver)





