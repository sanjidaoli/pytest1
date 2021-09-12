#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : test_contact1.py
@Project     : pytest1
@Time        : 2021/7/18 14:56
@Author      : LHQ
@Software    : PyCharm
"""
import yaml

from appium_wework.page.app import App
from appium_wework.page.move_screen import MoveScreen
import  pytest

class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()
    def teardown(self):
        self.app.stop()

    # @pytest.mark.parametrize('name,telno',[('lili',15012345671),('lilei',15012345672)])
    @pytest.mark.parametrize('name,telno',yaml.safe_load(open('./add.yaml',encoding='utf-8')))
    def test_addcontact(self,name,telno):
    # #     invitpage  = self.main.goto_addresslist().add_member().addmember_by_manul().input_name(name).set_gender().input_phonenum(telno).move_up().click_save()
        invitpage  = self.main.goto_addresslist().add_member().addmember_by_manul().input_name(name).set_gender().input_phonenum(telno).click_save()
        assert '成功' in invitpage.get_toast()

    @pytest.mark.parametrize('name,telno', yaml.safe_load(open('./add.yaml', encoding='utf-8')))
    def test_delcontact(self,name,telno):
        # delcontact = self.main.goto_addresslist().del_member(name).edit().edit_member().move_up().del_member()
        delcontact = self.main.goto_addresslist().del_member(name).edit().edit_member().del_member()