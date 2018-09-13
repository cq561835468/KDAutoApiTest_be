#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys,os,json,time
sys.path.append("../../../../")
sys.path.append(os.getcwd())
from model.REST.REST_main import REST_Request
from Fuction.Check_Point import CheckPoint
class Test_demo:
    def __init__(self,Test_Cases_name):
        global null
        null = ''
        #------------测试用例名称数组---------------
        self.Test_Cases_name = Test_Cases_name
        '''外部json数据名'''
        with open(os.path.dirname(os.path.realpath(__file__))+"\[DATA][Demo_Project][REST_Module_GET_POST]demo.json", 'r') as load_f:
            self.load_dict = json.load(load_f)
        '''外部数据文件名，包头'''
        self.TEST = CheckPoint(os.path.realpath(__file__),self.Test_Cases_name).Tests


    def Request(self):
        '''参数化执行测试用例'''
        '''包头'''
        head = {
            "Content-Type": "application/json",
        }
        for x in self.load_dict:
            '''包体'''
            body = {
                "userCode": x["userCode"],
                "userPassword": x["userPassword"]
            }
            self.Response_Api = REST_Request(name="[VIID][pic_many_mes][Get][Select][And]").run(method=x["method"],
                                                                                                url=x["url"],
                                                                                                port=x["port"],
                                                                                                path=x["path"],
                                                                                                head=head,
                                                                                                body=json.dumps(eval(json.dumps(body))))
            eva_Response_Api = eval(self.Response_Api.content) #格式转换
            sessionId = eva_Response_Api["sessionId"]
            self.Response_Api2 = REST_Request(name="[VIID][pic_many_mes][Get][Select][And]").run(method=x["method2"],
                                                                                                url=x["url"],
                                                                                                port=x["port"],
                                                                                                path=x["path2"]+sessionId,
                                                                                                head=head,
                                                                                                body=json.dumps(eval(json.dumps(body))))
            eva_Response_Api2 = eval(self.Response_Api2.content) #格式转换
            self.Response_Va(eva_Response_Api,x,Test_name=self.Test_Cases_name[0],
                             method=x["method"],
                             Res_Time=self.Response_Api.elapsed.microseconds /1000) #检查点1
            self.Response_Va2(eva_Response_Api2, x, Test_name=self.Test_Cases_name[1],
                              method=x["method2"],
                              Res_Time=self.Response_Api2.elapsed.microseconds /1000) #检查点2
    def Response_Va(self,response,para,Test_name,method,Res_Time):
        '''检查点'''
        self.TEST("=", "Status_code",Test_name,self.Response_Api.status_code, para["Re_State"],method,Res_Time)
        self.TEST("=", "resultCode", Test_name, response["resultCode"], para["resultCode"],method,Res_Time)
        self.TEST("=", "resultMsg", Test_name, response["resultMsg"].decode("utf-8"), para["resultMsg"],method,Res_Time)
        self.TEST("=", "ip", Test_name, response["ip"], para["ip"],method,Res_Time)
        # for x in response["user"]["privileges"]:
        #     self.TEST("=", "privilegeOrder", Test_name, x["privilegeOrder"], 3,method)

    def Response_Va2(self,response,para,Test_name,method,Res_Time):
        '''检查点'''
        self.TEST("=", "Status_code",Test_name,self.Response_Api.status_code, para["Re_State"],method,Res_Time)
        self.TEST("=", "resultCode", Test_name, response["resultCode"], para["resultCode"],method,Res_Time)
        self.TEST("=", "resultMsg", Test_name, response["resultMsg"].decode("utf-8"), para["resultMsg"],method,Res_Time)

try:
    demo = Test_demo(["vc_login","vc_get_address"]).Request()
except Exception, e:
    print e
    CheckPoint(os.path.realpath(__file__), ["vc_login","vc_get_address"]).error(os.path.realpath(__file__))
    #errors()