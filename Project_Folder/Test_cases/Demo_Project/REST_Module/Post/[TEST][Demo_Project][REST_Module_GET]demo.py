#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys,os,json,time
sys.path.append("../../../../")
sys.path.append(os.getcwd())
from model.REST.REST_main import REST_Request
from Fuction.Check_Point import CheckPoint
class Test_demo:
    def __init__(self):
        global null
        null = ''
        #------------测试用例名称数组---------------
        self.Test_Cases_name = ["vc_login"]
        '''外部数据文件名，包头'''
        self.TEST = CheckPoint(os.path.realpath(__file__),self.Test_Cases_name).Tests
        #------------外部json数据名---------------------
        with open(os.path.dirname(os.path.realpath(__file__))+"\[DATA][Demo_Project][REST_Module_GET]demo.json", 'r') as load_f:
            self.load_dict = json.load(load_f)

    def Request(self):
        '''参数化执行测试用例'''
        #---------------包头------------------
        head = {
            "Content-Type": "application/json",
        }
        #-------------------------------------
        for x in self.load_dict:
            #---------------包体--------------
            body = {
                "userCode": x["userCode"],
                "userPassword": x["userPassword"]
            }
            #----------------------------------
            self.Response_Api = REST_Request(name="[VIID][pic_many_mes][Get][Select][And]").run(method=x["method"],
                                                                                                url=x["url"],
                                                                                                port=x["port"],
                                                                                                path=x["path"],
                                                                                                head=head,
                                                                                                body=json.dumps(eval(json.dumps(body))))
            eva_Response_Api = eval(self.Response_Api.content) #格式转换
            #self.Response_Va(eva_Response_Api,  x,  Test_name=self.Test_Cases_name[0]) #检查点1
    def Response_Va(self,response,para,Test_name):
        '''检查点编写alias为输出到报告中测试集的名称'''
        #-----------------------检查点编写-------------------------------
        self.TEST("=", "Status_code",Test_name,self.Response_Api.status_code, para["Re_State"])
        self.TEST("=", "resultCode", Test_name, response["resultCode"], para["resultCode"])
        self.TEST("=", "resultMsg", Test_name, response["resultMsg"].decode("utf-8"), para["resultMsg"])
        self.TEST("=", "ip", Test_name, response["ip"], para["ip"])
        for x in response["user"]["privileges"]:
            self.TEST("=", "privilegeOrder", Test_name, x["privilegeOrder"], 3)

demo = Test_demo().Request()