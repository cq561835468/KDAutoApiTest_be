#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Project_Folder.Fuction.logging_class import Logger
from Fuction.SOAP_Project import SOAP_Project
import os
import datetime

#path = os.path.dirname(os.path.realpath(__file__))

class SOAP_Request():
    def __init__(self,name):
        self.name = name
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H')
        logobj = Logger(os.getcwd() + r'\Logs' + '\\' + time + '\\'+name+'.log')
        logobj.debug("SOAP_main begin")
    def run(self,method,url,port,path=None,head=None,body=None):
        if method == "POST":
            return SOAP_Project(self.name).POST(url, port, path, head, body)