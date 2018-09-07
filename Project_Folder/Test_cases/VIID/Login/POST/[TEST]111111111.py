#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys,os
sys.path.append("../../../../")
sys.path.append(os.getcwd())
from model.REST.REST_main import REST_Request

class Test_demo:
    def __init__(self):
        pass
    def Request(self):
        self.Response_Api = REST_Request().run("POST","172.16.121.25","5088","/baidu.post",5,6)
        print self.Response_Api
    def Response_Va(self):
        pass

demo = Test_demo().Request()
print demo