#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Project_Folder.Fuction.logging_class import Logger
from Fuction.WebSocket_Project import WebSocket_Project
import os
import datetime

#path = os.path.dirname(os.path.realpath(__file__))

class WebSocket_Request():
    def __init__(self,name):
        self.name = name
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H')
        logobj = Logger(os.getcwd() + r'\Logs' + '\\' + time + '\\'+name+'.log')
        logobj.debug("WebSocket_main begin")
    def run(self,method,url,port,path=None,head=None,body=None):
        if method == "POST":
            return WebSocket_Project(self.name).Sock_Send(url, port, path, head, body)