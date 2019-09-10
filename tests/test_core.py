#!usr/bin/env python
#-*- coding:utf-8 -*-

import requests

from apitest.api import BaseApi


class ApihttbinGet(BaseApi):
    url = "http://httpbin.org/get"
    params={}
    method = "GET"
    headers = {"accept":"application/json"}
    data = ""
    json = {}

def test_httpbin_get():
    ApihttbinGet().run() \
        .validate("status_code", 200)

def test_httpbin_get_with_params():
    ApihttbinGet()\
        .set_params(abc=123,xyz=456)\
        .run()\
        .validate("status_code",200)

class ApihttpbinPost(BaseApi):
    url = "http://httpbin.org/post"
    method = "POST"
    params = {}
    headers = {"accept": "application/json"}
    data = "abc=123"
    json = {"abc":123}

def test_httpbin_post():
    ApihttpbinPost().set_json({"abc":456}).run().validate("status_code", 200)
