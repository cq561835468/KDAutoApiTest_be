#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from Project_Folder.Fuction.logging_class import Logger
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
paths = path +r'\Logs\REST_Project.conf'
logobj = Logger(paths)
logobj.debug("test_begin")

class REST_Project():
    def __init__(self):
        pass
    def GET(self,url,port,path,head):
        '''发送GET请求'''
        #print url,port,path,head
        return "GET"

    def POST(self,url,port,path,head,body):
        '''发送POST请求'''
        #print url,port,path,head,body
        #print "i am POST"
        return "POST"

    def PUT(self,url,port,path,head,body):
        '''发送PUT请求'''
        #print url,port,path,head,body
        return "PUT"

    def DELETE(self,url,port,path,head,body):
        '''发送DELETE请求'''
        #print url,port,path,head,body
        return "DELETE"