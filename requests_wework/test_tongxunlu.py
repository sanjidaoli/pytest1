#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Description : 
@File        : test_tongxunlu.py
@Project     : pytest1
@Time        : 2021/9/11 18:23
@Author      : LHQ
@Software    : PyCharm
"""
import random
import re

import pytest
import requests
from filelock import FileLock


@pytest.fixture(scope="session")
def test_gettoken():
    res = None
    # while FileLock("session.lock"):
    corpid = 'wwc2d69ffd3be502bb'
    corpsecret = '5ClQxWwCtRk4DHiNRHEHgODPm79tsmZ-GAb3ChjUsrM'
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    print(res.json()["access_token"])
    return res.json()["access_token"]
def test_getmember(userid,test_gettoken):
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_gettoken}&userid={userid}')
    print(res.json())
    return  res.json()

def test_addmember(userid,name,mobile,test_gettoken):
    data = {
        "userid":userid,
        "name":name,
        "mobile":mobile,
        "department":[1]
    }
    res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_gettoken}',json=data)
    print(res.json())
    return res.json()
def test_updatemeber(userid,name,mobile,test_gettoken):
    data = {
        "userid":userid,
        "name":name,
        "mobile":mobile,
        "department": [1]
    }
    res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_gettoken}', json=data)
    print(res.json())
    return  res.json()

def test_delmeber(userid,test_gettoken):
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_gettoken}&userid={userid}')
    print(res.json())
    return  res.json()

def test_create_data():
    # data = [(str(random.randint(0,999999)),"zhangsan",str(random.randint(15012345600,15012345699))) for x in range(10)]
    data = [("zs123"+ str(x),"zhangsan","138%08d" % x)for x in range(20)]
    print(data)
    return data

# @pytest.mark.parametrize("userid,name,mobile",[("zhangsan","张三","15012345671")])

@pytest.mark.parametrize("userid,name,mobile",test_create_data())
def test_all(userid,name,mobile,test_gettoken):
    try:
        assert  "created" == test_addmember(userid,name,mobile,test_gettoken)["errmsg"]
    except AssertionError as e:
        if "mobile existed" in e.__str__():
            re_userid = re.findall(":(.*)'$'",e.__str__()[0])
            assert "deleted" == test_delmeber(userid,test_gettoken)["errmsg"]
            assert 60111 == test_getmember(userid,test_gettoken)["errcode"]
            assert "created" == test_addmember(userid, name, mobile,test_gettoken)["errmsg"]

    assert  name == test_getmember(userid,test_gettoken)["name"]
    assert  "updated" == test_updatemeber(userid,"张四",mobile,test_gettoken)["errmsg"]
    assert "张四" == test_getmember(userid,test_gettoken)["name"]
    assert  "deleted" == test_delmeber(userid,test_gettoken)["errmsg"]
    assert 60111 == test_getmember(userid,test_gettoken)["errcode"]