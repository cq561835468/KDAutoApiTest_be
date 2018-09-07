#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Project_Folder.Fuction.logging_class import Logger
from Fuction.REST_Project import REST_Project
import os

path = os.path.dirname(os.path.realpath(__file__))

logobj = Logger(path + r'\Logs\Rest_main.logs')
logobj.debug("REST_main begin")
logobj.debug("REST_main end")

class REST_Request():
    def __init__(self):
        pass
    def run(self,method,url,port,path,head,body):
        if method == "GET":
            return REST_Project().GET(url, port, path, head)
        elif method == "POST":
            #print REST_Project().POST(url, port, path, head, body)
            return REST_Project().POST(url, port, path, head, body)
        elif method == "PUT":
            return REST_Project().PUT(url, port, path, head, body)
        elif method == "DELETE":
            return REST_Project().DELETE(url, port, path, head, body)