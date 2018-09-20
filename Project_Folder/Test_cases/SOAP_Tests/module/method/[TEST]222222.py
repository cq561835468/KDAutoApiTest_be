#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys,os,json,pprint
#sys.path.append("../../../../")
sys.path.append(os.getcwd())
from model.SOAP.SOAP_main import SOAP_Request
from Fuction.Check_Point import CheckPoint
class Test_demo:
    def __init__(self):
        '''外部数据文件名，包头'''
        with open(os.path.dirname(os.path.realpath(__file__))+"\[DATA]222222.json", 'r') as load_f:
            self.load_dict = json.load(load_f)
        self.head = {
            "Content-Type": "application/xml",
        }
    def Request(self):
        for x in self.load_dict:
            '''参数化'''
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
            self.Response_Api = SOAP_Request(name="test_api").run(method=x["method"],url=x["url"],port=x["port"],path=x["path"],body=body,head=self.head)
            self.Response_Va(eval(self.Response_Api), x)
    def Response_Va(self,response,para):
        '''检查点编写'''
        #TEST = CheckPoint().Tests #实例化|判断，原始数据，预期数据
        pass
        #TEST("=","cusdk:cuUpdateUrl",response["SOAP-ENV:Envelope"]["SOAP-ENV:Body"]["cusdk:LoginRsp"]["cusdk:cuUpdateUrl"],para["cusdk:cuUpdateUrl"])
        #TEST("!=","cusdk:passwordRemainTime", response["SOAP-ENV:Envelope"]["SOAP-ENV:Body"]["cusdk:LoginRsp"]["cusdk:passwordRemainTime"],para["cusdk:passwordRemainTime"])
demo = Test_demo().Request()