#!usr/bin/env python
#-*- coding:utf-8 -*-

import requests

class BaseApi(object):
    pass

class ApihttbinGet(BaseApi):
    url = "http://httpbin.org/get"
    params=None
    method = "GET"
    headers = {"accept":"application/json"}

    def set_params(self,**params):
        self.params = params
        return self

    def run(self):
        self.response = requests.get(
            self.url,
            headers=self.headers,
            params=self.params)
        return self

    def validate(self,key,expected_value):
        actual_value = getattr(self.response,key)
        assert actual_value == expected_value
        return self

class ApihttpbinPost(BaseApi):
    url = "http://httpbin.org/post"
    method = "POST"
    headers = {"accept": "application/json"}
    json = {"abc":123}

    ApihttbinGet().run()\
        .validate("status_code",200)
        # .validate("headers.server","nginx")\
        # .validate("json.url","http://httpbin.org/post")

def test_httpbin_get():
    # resp=requests.get("http://httpbin.org/get",
    #          headers={"accept":"application/json"}
    #          )
    # assert resp.status_code==200
    ApihttbinGet().run() \
        .validate("status_code", 200)
    # .validate("headers.server","nginx")\
    # .validate("json.url","http://httpbin.org/post")

def test_httpbin_get_with_params():
    ApihttbinGet().set_params(abc=123,xyz=456)\
        .run()\
        .validate("status_code",200)

