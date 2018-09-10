#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Project_Folder.Fuction.logging_class import Logger
from Fuction.REST_Project import REST_Project
import os
import datetime

#path = os.path.dirname(os.path.realpath(__file__))
time = datetime.datetime.now().strftime('%Y-%m-%d_%H')
logobj = Logger(os.getcwd() + r'\Logs'+'\\'+time+'\Rest.log')
logobj.debug("REST_main begin")
logobj.debug("REST_main end")

class REST_Request():
    def __init__(self):
        pass
    def run(self,method,url,port,path=None,head=None,body=None):
        if method == "POST":
            return REST_Project().POST(url, port, path, head, body)