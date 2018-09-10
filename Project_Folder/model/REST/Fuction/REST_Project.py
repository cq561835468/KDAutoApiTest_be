#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import requests
import datetime
from Project_Folder.Fuction.logging_class import Logger
#path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
time = datetime.datetime.now().strftime('%Y-%m-%d_%H')
logobj = Logger(os.getcwd() + r'\Logs'+'\\'+time+'\Rest.log')
logobj.debug("REST_Project Begin")
logobj.debug("REST_Project End")

class REST_Project():
    def __init__(self):
        pass
    def GET(self,url,port=80,path="/",head=None):
        '''发送GET请求'''
        response = requests.request("GET", str(url) + ':' + str(port) + '/' + path, headers=head)
        return response.content

    def POST(self,url,port,path,head,body):
        '''发送POST请求'''
        response = requests.request("POST", str(url)+':'+str(port)+'/'+path, data=body, headers=head)
        return response.content

    def PUT(self,url,port,path,head,body):
        '''发送PUT请求'''
        response = requests.request("PUT", str(url)+':'+str(port)+'/'+path, data=body, headers=head)
        return response.content

    def DELETE(self,url,port,path,head,body):
        '''发送DELETE请求'''
        response = requests.request("DELETE", str(url)+':'+str(port)+'/'+path, data=body, headers=head)
        return response.content