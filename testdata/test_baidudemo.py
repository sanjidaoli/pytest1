#!/usr/bin/env python
# _*_ coding: utf-8  _*_
import  allure
import pytest
import  yaml
from selenium import webdriver
import time


@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1',yaml.safe_load(open("testdata/baidudata.yml")))
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver =  webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜索词: {test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./tmp/result/b.png")
        allure.attach.file("./tmp/result/b.png",attachment_type=allure.attachment_type.PNG)
    with allure.step("关闭浏览器"):
        driver.quit()


