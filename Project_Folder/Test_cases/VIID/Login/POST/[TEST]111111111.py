#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys,os,json
sys.path.append("../../../../")
sys.path.append(os.getcwd())
from model.REST.REST_main import REST_Request

class Test_demo:
    def __init__(self):
        '''外部数据文件名，包头'''
        with open("[DATA]1111111.json", 'r') as load_f:
            self.load_dict = json.load(load_f)
        self.head = {
            "Content-Type": "application/json",
        }
    def Request(self):
        for x in self.load_dict:
            '''参数化'''
            #--------------------------
            body = {
                "word": x["word"],
                "from": x["from"],
                "to": x["to"]
            }
            #----------------------------
            self.Response_Api = REST_Request().run(x["method"],x["url"],x["port"],x["path"],self.head,json.dumps(eval(json.dumps(body))))
            self.Response_Va(eval(self.Response_Api.content),x)
    def Response_Va(self,response,para):
        '''检查点编写'''
        self.TEST("=",response["to"],para["to"])
        self.TEST("=", response["from"], para["from"])
        self.TEST("=", response["trans_result"][0]["src"], para["word"])

    def TEST(self,char,data1,data2):
        if char == "=":
            if data1 == data2:
                print "checkpoint pass"
        elif char == "<":
            if data1 < data2:
                print "checkpoint pass"
        elif char == "<="or char == "=<":
            if data1 <= data2:
                print "checkpoint pass"
        elif char == ">":
            if data1 > data2:
                print "checkpoint pass"
        elif char == ">=" or char == "=>":
            if data1 > data2:
                print "checkpoint pass"
demo = Test_demo().Request()