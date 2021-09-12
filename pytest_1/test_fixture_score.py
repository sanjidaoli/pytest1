#！/usr/bin/env python
#！-*- coding:utf-8 -*-
import  pytest

#作用域:module 是在模块执行之前执行，模块之后执行
@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield

    print("执行 teardown !")
    print("关闭浏览器")

@pytest.mark.usefixtures("open")
def test_serch1():
    print("test_search1")
    raise NameError
    pass

def test_search2(open):
    print("test_search2")
    pass

def test_search3(open):
    print("test_serach3")
    pass
