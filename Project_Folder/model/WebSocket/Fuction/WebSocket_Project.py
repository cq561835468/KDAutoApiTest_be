#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import datetime

from Project_Folder.Fuction.logging_class import Logger
from websocket import create_connection

#path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class WebSocket_Project():
    def __init__(self,name):
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H')
        self.logobj = Logger(os.getcwd() + r'\Logs' + '\\' + time + '\\'+name+'.log')
        self.logobj.debug("WebSocket_Project Begin")

    def Sock_Send(self,url, port, path, head, body):
        ws = create_connection("ws://172.16.120.22:8181/endpoint4651")
        re = ws.send("{\"endpoint\":{\"type\":\"offerer\",\"connection\":\"208\"},\"message\":{\"status\":\"connected\"}}")
        print ws.recv()
        #print ws.status
        #print ws.recv_data()
        self.logobj.debug("WebSocket_Project End")
        self.logobj.debug("WebSocket_main End")
        ws.close()


