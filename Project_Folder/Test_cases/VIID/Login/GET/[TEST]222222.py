#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys,os,json
sys.path.append("../../../../")
sys.path.append(os.getcwd())
from model.REST.REST_main import REST_Request
from Fuction.Check_Point import CheckPoint
class Test_demo:
    def __init__(self):
        '''外部数据文件名，包头'''
        with open(os.path.dirname(os.path.realpath(__file__))+"\[DATA]222222.json", 'r') as load_f:
            self.load_dict = json.load(load_f)
        self.head = {
            "Content-Type": "application/json",
        }
    def Request(self):
        for x in self.load_dict:
            '''参数化'''
            self.Response_Api = REST_Request().run(method=x["method"],url=x["url"],port=x["port"],path=x["path"],head=self.head)
            self.Response_Va(eval(self.Response_Api),x)
    def Response_Va(self,response,para):
        '''检查点编写'''
        TEST = CheckPoint().Tests #实例化|判断，原始数据，预期数据
        TEST("=","to",response["to"],para["to"])
        TEST("=","from", response["from"], para["from"])
        TEST("=","trans_result", response["trans_result"][0]["src"], para["word"])

demo = Test_demo().Request()