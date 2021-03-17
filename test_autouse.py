#！/usr/bin/env python
#！-*- coding:utf-8 -*-
import  pytest
@pytest.fixture(autouse="true")
def myfixture():
    print("this is my fixture")

class TestAutoUse:
    def test_one(self):
        print("执行 test_one")
        assert  1 + 2  == 3

    def test_two(self):
        print("执行 test_two")
        assert 1  == 1

    def test_three(self):
        print("执行 test_three")
        assert  1 + 1 == 2