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
		.validate("headers.server","nginx")\
		.validate("json().url", "https://httpbin.org/post")\
		.validate("json().json.abc",456)

def test_httpbin_parameters_share():
	#单个测试接口参数共享
	user_id="jdk129"
	ApihttbinGet()\
		.set_params(user_id=user_id)\
		.run()\
		.validate("status_code", 200)\
		.validate("headers.server", "nginx")\
		.validate("json().url", "https://httpbin.org/get?user_id={}".format(user_id))

	ApihttpbinPost()\
		.set_json({"user_id": user_id})\
		.run()\
		.validate("status_code", 200)\
		.validate("headers.server", "nginx")\
		.validate("json().url", "https://httpbin.org/post")\
		.validate("json().json.user_id", "jdk129")


def test_httpbin_extract():
	api_run = ApihttbinGet().run()
	status_code = api_run.extract("status_code")
	assert status_code == 200

	server = api_run.extract("headers.server")
	assert  server == "nginx"

	accept_type = api_run.extract("json().headers.Accept")
	assert accept_type == "application/json"


def test_httpbin_setcookies():
	api_run = ApihttpbinGetCookies()\
		.set_cookie("freeform1","123")\
		.set_cookie("freeform2","456")\
		.run()
	freeform1 = api_run.extract("json().cookies.freeform1")
	freeform2 = api_run.extract("json().cookies.freeform2")
	assert freeform1 == "123"
	assert freeform2 == "456"


def test_httpbin_parameters_extract():
	#接口参数依赖
	#step1:get value
	freeform = ApihttpbinGetCookies()\
		.set_cookie("freeform","123")\
		.run()\
		.extract("json().cookies.freeform")
	assert freeform == "123"

	#step2:use value as parameter
	ApihttpbinPost() \
		.set_json({"freeform": freeform})\
		.run()\
		.validate("status_code", 200) \
		.validate("headers.server", "nginx") \
		.validate("json().url", "https://httpbin.org/post") \
		.validate("json().json.freeform", freeform)

def test_httpbin_login_status():
	#step1:login and get cookie
	ApihttpbinSetCookies().set_params(freeform="123").run()

	#step2:
	resp = ApihttpbinPost() \
		.set_json({"abc": 123}) \
		.run().get_response()
	request_headers = resp.request.headers
	assert 'freeform=123' in request_headers["Cookie"]
	print("request_headers====",request_headers)