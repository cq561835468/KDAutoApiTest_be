#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Project_Folder.Fuction.logging_class import Logger
from Fuction.REST_Project import REST_Project
import os
import datetime

#path = os.path.dirname(os.path.realpath(__file__))

class REST_Request():
    def __init__(self, name):
        self.name = name
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H')
        logobj = Logger(os.getcwd() + r'\Logs' + '\\' + time + '\\'+name+'.log')
        logobj.debug("REST_main begin")
    def run(self,method,url,port,path=None,head=None,body=None):
        if method == "GET":
            return REST_Project(self.name).GET(url, port, path, head)
        if method == "POST":
            return REST_Project(self.name).POST(url, port, path, head, body)
        if method == "PUT":
            return REST_Project(self.name).PUT(url, port, path, head, body)
        if method == "DELETE":
            return REST_Project(self.name).DELETE(url, port, path, head, body)