#!usr/bin/env python
#-*- coding:utf-8 -*-

import pytest
import requests

@pytest.fixture
def init_session():
	return requests.sessions.session()