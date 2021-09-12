#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : test_alert.py
@Project     : pytest1
@Time        : 2021/4/10 23:20
@Author      : LHQ
@Software    : PyCharm
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium1.Base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag_elemnent = self.driver.find_element_by_id("draggable")
        # drag_elemnent = self.driver.find_element(By.ID,"draggable")
        drop_elemnent = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_elemnent,drop_elemnent).perform()
        # action.click_and_hold(drag_elemnent).release(drop_elemnent).perform()
        # action.click_and_hold(drag_elemnent).move_to_element(drop_elemnent).release().perform()
        print("点击alert确认")
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        time.sleep(3)
