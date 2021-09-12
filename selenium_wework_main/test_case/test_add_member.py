#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : test_add_member.py
@Project     : pytest1
@Time        : 2021/5/1 22:15
@Author      : LHQ
@Software    : PyCharm
"""
from time import sleep

import pytest

from selenium_wework_main.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_addmember(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        sleep(3)
        assert "hello" in  add_member.get_member()

    @pytest.mark.skip
    def test_addmember1(self):
        add_member1 = self.main.goto_menu_contacts().goto_add_member1()
        add_member1.add_member()
        sleep(2)
        assert "hello" in  add_member1.get_member()

    def test_split(self):
        a= '1/10'
        print(a.split('/', 1))
