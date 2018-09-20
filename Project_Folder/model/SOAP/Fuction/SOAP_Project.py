#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import requests
import datetime
import xmltodict
import json

from Project_Folder.Fuction.logging_class import Logger
#path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class SOAP_Project():
    def __init__(self,name):
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H')
        self.logobj = Logger(os.getcwd() + r'\Logs' + '\\' + time + '\\'+name+'.log')
        self.logobj.debug("SOAP_Project Begin")

    def xmltojson(self,xmlstr):
        # parse是的xml解析器
        xmlparse = xmltodict.parse(xmlstr)
        # json库dumps()是将dict转化成json格式，loads()是将json转化成dict格式。
        # dumps()方法的ident=1，格式化json
        jsonstr = json.dumps(xmlparse, indent=1)
        #print(jsonstr)
        return jsonstr

    def POST(self,url,port,path,head,body):
        '''发送POST请求'''
        response = requests.request("POST", str(url)+':'+str(port)+path, data=body, headers=head)
        self.logobj.debug("SOAP_Project End")
        self.logobj.debug("SOAP_main End")
        return [self.xmltojson(response.content),response]
