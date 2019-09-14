#!usr/bin/env python
#-*- coding:utf-8 -*-
from apitest.api import BaseApi


class ApihttbinGet(BaseApi):
    url = "http://httpbin.org/get"
    params={}
    method = "GET"
    headers = {"accept":"application/json"}
    data = ""
    json = {}

class ApihttpbinPost(BaseApi):
    url = "http://httpbin.org/post"
    method = "POST"
    params = {}
    headers = {"accept": "application/json"}
    data = "abc=123"
    json = {"abc":123}