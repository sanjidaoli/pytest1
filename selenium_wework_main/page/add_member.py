#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : add_member.py
@Project     : pytest1
@Time        : 2021/5/1 22:01
@Author      : LHQ
@Software    : PyCharm
"""
from time import sleep


#企业微信添加成员页
from selenium.webdriver.common.by import By

from selenium_wework_main.page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        self._driver.find_element(By.ID,'username').send_keys("hello")
        self._driver.find_element(By.ID, 'memberAdd_english_name').send_keys("LILEI")
        self._driver.find_element(By.ID,'memberAdd_acctid').send_keys("hello123")
        self._driver.find_element(By.ID, 'memberAdd_phone').send_keys("15012345678")
        self._driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
 
        # # self._driver.find_element_by_id('username').send_keys("hello")
        # self._driver.find_element_by_id('memberAdd_english_name').send_keys("LILEI")
        # self._driver.find_element_by_id('memberAdd_acctid').send_keys("hello123")
        # self._driver.find_element_by_id('memberAdd_phone').send_keys("15012345678")
        # self._driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]").click()
        return  True
    def get_member(self):
        sleep(3)
        elements = self._driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        # elements = self._driver.find_elements_by_css_selector('.member_colRight_memberTable_td:nth-child(2)')

        content:str = self.find(By.CSS_SELECTOR,'fenye').text
        cur_page,total_page = [int(x) for x in contene.split('/',1)]
        list = []
        while True:
            elements = self._driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
            for element in elements:
                list.append(element.get_attribute("title"))
            content: str = self.find(By.CSS_SELECTOR, 'fenye').text
            cur_page = [int(x) for x in contene.split('/', 1)][0]
            if cur_page == total_page:
                return  list
            self._driver.find_element(By.CSS_SELECTOR,'fanye').click()



        list = [element.get_attribute("title") for element in elements]
        return  list