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
        '''测试用例命名'''
        self.Test_Cases_name = ["vc_login"]
        '''外部数据获取'''
        self.file_out = self.Get_Json("[DATA][De1212.json")
        '''实例化'''
        self.CP = CheckPoint(os.path.realpath(__file__), self.Test_Cases_name,len(self.file_out))

    def Get_Json(self,filename):
        '''读取外部数据'''
        with open(os.path.dirname(os.path.realpath(__file__))+"\\"+filename, 'r') as load_f:
            load_dict = json.load(load_f)
        return load_dict

    def Request(self):
        '''参数化执行测试用例'''
        '''包头'''
        try:
            head = {
                "Content-Type": "application/json",
            }
            for x in self.file_out:
                '''包体'''
                self.CP.Init_Json() #每次都数据化临时json报告
                body = {
                    "userCode": x["userCode"],
                    "userPassword": x["userPassword"]}

                self.Response_Api = REST_Request(name="[VIID][pic_many_mes][Get][Select][And]").run(method=x["method"],
                                                                                                    url=x["url"],
                                                                                                    port=x["port"],
                                                                                                    path=x["path"],
                                                                                                    head=head,
                                                                                                    body=json.dumps(eval(json.dumps(body))))
                eva_Response_Api = eval(self.Response_Api.content) #格式转换

                self.Response_Va(eva_Response_Api,x,Test_name=self.Test_Cases_name[0], #用例名称1
                                 method=x["method"], #请求
                                 Res_Time=self.Response_Api.elapsed.microseconds /1000,
                                 Res_State=self.Response_Api.status_code) #响应时间
                self.CP.Init_Json_Last("append") #将完成的json报告增加到最终报告中
        except Exception, e:
            print 'str(Exception):\t', str(Exception)
            print 'str(e):\t\t', str(e)
            print 'repr(e):\t', repr(e)
            print 'e.message:\t', e.message
            self.CP.Init_Json()
            self.CP.error(os.path.realpath(__file__))
            self.CP.Init_Json_Last("append")
    def Response_Va(self,response,para,Test_name,method,Res_Time,Res_State):
        '''检查点'''
        print "Test_name is " + Test_name
        self.CP.Tests("=", "Status_code",Test_name,self.Response_Api.status_code, para["Re_State"],method,Res_Time,Res_State)
        self.CP.Tests("=", "resultCode", Test_name, response["resultCode"], para["resultCode"],method,Res_Time,Res_State)
        self.CP.Tests("=", "resultMsg", Test_name, response["resultMsg"].decode("utf-8"), para["resultMsg"],method,Res_Time,Res_State)

demo = Test_demo().Request()

