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
        self.TEST = CheckPoint(os.path.realpath(__file__)).Tests  # 实例化|判断，原始数据，预期数据
        with open(os.path.dirname(os.path.realpath(__file__))+"\[DATA][VIID][pic_many_mes][Get][Select][And].json", 'r') as load_f:
            self.load_dict = json.load(load_f)

    def Request(self):
        head = {
            "Content-Type": "application/json",
        }
        '''参数化执行测试用例'''
        for x in self.load_dict:
            self.Response_Api = REST_Request(name="[VIID][pic_many_mes][Get][Select][And]").run(method=x["method"],url=x["url"],port=x["port"],path=x["path"],head=head)
            self.Response_Va(eval(self.Response_Api.content),x,Test_name="pic_many_mes")
    def Response_Va(self,response,para,Test_name):
        '''检查点编写alias为输出到报告中测试集的名称'''
        self.TEST("=", "Status_code",Test_name,self.Response_Api.status_code, 200)
        #TEST("=","to",response["to"],para["to"])
        #TEST("=","from", response["from"], para["from"])
        #TEST("=","trans_result", response["trans_result"][0]["src"], para["word"])

demo = Test_demo().Request()