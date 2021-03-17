#！/usr/bin/env python
#！-*- coding:utf-8 -*-
import  pytest

@pytest.fixture(scope="session")
def open():
    print("浏览器")
    yield

    print("执行 teardwon !")
    print("最后关闭浏览器")