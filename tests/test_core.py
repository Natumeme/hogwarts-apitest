#!usr/bin/env python
#-*- coding:utf-8 -*-

from tests.api.httpbin import *


def test_httpbin_get():
	ApihttbinGet().run()\
		.validate("status_code", 200)\
		.validate("headers.server", "nginx")\
		.validate("json().url", "https://httpbin.org/get")\
		.validate("json().args", {})\
		.validate("json().headers.Accept", "application/json")

def test_httpbin_get_with_params():
	ApihttbinGet()\
		.set_params(abc=123,xyz=456)\
		.run()\
		.validate("status_code",200)\
		.validate("headers.server", "nginx")


def test_httpbin_post():
	ApihttpbinPost()\
		.set_json({"abc":456})\
		.run()\
		.validate("status_code", 200)\
		.validate("headers.server","nginx") \
		.validate("json().url", "https://httpbin.org/post")\
		.validate("json().json.abc",456)

def test_httpbin_parameters_share():
	user_id="jdk129"
	ApihttbinGet() \
		.set_params(user_id=user_id) \
		.run() \
		.validate("status_code", 200) \
		.validate("headers.server", "nginx") \
		.validate("json().url", "https://httpbin.org/get?user_id={}".format(user_id))

	ApihttpbinPost() \
		.set_json({"user_id": user_id}) \
		.run() \
		.validate("status_code", 200) \
		.validate("headers.server", "nginx")\
		.validate("json().url", "https://httpbin.org/post")\
		.validate("json().json.user_id", "jdk129")
