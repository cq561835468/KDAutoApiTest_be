#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys,os,json,time,traceback
#sys.path.append("../../../../")
sys.path.append(os.getcwd())
from model.SOAP.SOAP_main import SOAP_Request
from Fuction.Check_Point import CheckPoint
class Test_demo:
    def __init__(self):
        # global null
        # null = ''
        '''测试用例命名'''
        self.Test_Cases_name = ["[TEST]CU"]
        '''外部数据获取'''
        self.file_out = self.Get_Json("[DATA]CU[Login].json")
        '''实例化'''
        self.CP = CheckPoint(os.path.realpath(__file__), self.Test_Cases_name,len(self.file_out))
        #self.RM_Append_JSON = CheckPoint(os.path.realpath(__file__), self.Test_Cases_name).RM_Append_JSON
        #self.TEST = self.CP.Tests

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
                "Content-Type": "application/xml",
            }
            for x in self.file_out:
                '''包体'''
                self.CP.Init_Json() #每次都数据化临时json报告
                body = '''<?xml version="1.0" encoding="UTF-8"?>
                            <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" 
                            xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" 
                            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
                            xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
                            xmlns:cusdk="urn:cusdk">
                                <SOAP-ENV:Body>
                                    <cusdk:Login>
                                        <cusdk:loginReq>
                                            <cusdk:userName>admin@kadacom</cusdk:userName>
                                            <cusdk:password>kedacom123</cusdk:password>
                                            <cusdk:cusdkVersion>2.0</cusdk:cusdkVersion>
                                            <cusdk:clientType>cuver</cusdk:clientType>
                                            <cusdk:isSupportNA>false</cusdk:isSupportNA>
                                            <cusdk:webCUClientAddr>
                                            </cusdk:webCUClientAddr>
                                        </cusdk:loginReq>
                                    </cusdk:Login>
                                </SOAP-ENV:Body>
                            </SOAP-ENV:Envelope>'''
                self.Response_Api = SOAP_Request(name="test_api").run(method=x["method"], url=x["url"], port=x["port"],path=x["path"], body=body, head=head)
                eva_Response_Api = eval(self.Response_Api[0]) #格式转换
                self.Response_Va(eva_Response_Api,x,Test_name=self.Test_Cases_name[0], #用例名称1
                                 method=x["method"], #请求
                                 Res_Time=self.Response_Api[1].elapsed.microseconds /1000)

                self.CP.Init_Json_Last("append") #将完成的json报告增加到最终报告中
        except Exception, e:
            print 'str(Exception):\t', str(Exception)
            print 'str(e):\t\t', str(e)
            print 'repr(e):\t', repr(e)
            print 'e.message:\t', e.message
            print 'traceback.print_exc():';
            traceback.print_exc()
            print 'traceback.format_exc():\n%s' % traceback.format_exc()
            self.CP.Init_Json()
            self.CP.error(os.path.realpath(__file__))
            self.CP.Init_Json_Last("append")
    def Response_Va(self,response,para,Test_name,method,Res_Time):
        '''检查点'''
        self.CP.Tests("=", "Status_code",Test_name,self.Response_Api[1].status_code, para["Re_State"],method,Res_Time,self.Response_Api[1].status_code)
        self.CP.Tests("=", "Status_code", Test_name, self.Response_Api[1].status_code, para["Re_State"], method,Res_Time, self.Response_Api[1].status_code)
        self.CP.Tests("=", "Status_code", Test_name, self.Response_Api[1].status_code, para["Re_State"], method,Res_Time, self.Response_Api[1].status_code)
        self.CP.Tests("=", "Status_code", Test_name, self.Response_Api[1].status_code, para["Re_State"], method,
                      Res_Time, self.Response_Api[1].status_code)

demo = Test_demo().Request()

