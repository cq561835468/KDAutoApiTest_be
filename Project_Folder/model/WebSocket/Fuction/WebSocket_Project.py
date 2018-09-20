#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import datetime
import time

from Project_Folder.Fuction.logging_class import Logger
from websocket import create_connection

#path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class WebSocket_Project():
    def __init__(self,name):
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H')
        # self.logobj = Logger(os.getcwd() + r'\Logs' + '\\' + time + '\\'+name+'.log')
        # self.logobj.debug("WebSocket_Project Begin")

    def Sock_Create_One(self,url, port, path, body, timeout):
        # print str(url)+":"+str(port)+str(path)
        # print body
        try:
            wsa = create_connection(str(url)+":"+str(port)+str(path),timeout=timeout)
            arrw = []
            for x in body:
                wsa.send(x)
            for x in range(0,99):
                arrw.append(wsa.recv())
            wsa.close()
            return arrw
        except:
            return arrw

    def Sock_Create_EveryOne(self,url, port, path, body, timeout):
        arrw = []
        for x in body:
            try:
                wsa = create_connection(str(url) + ":" + str(port) + str(path), timeout=timeout)
                wsa.send(x)
                for x in range(0,99):
                    arrw.append(wsa.recv())
            except:
                wsa.close()
                continue
        return arrw

    def Sock_DELETE(self,url, port, path, body, body2):
        # print str(url)+":"+str(port)+str(path)
        # print "body is %s" % body
        wsa = create_connection("ws://172.16.120.22:8181/endpoint8735")
        a = '''request:1\r\nmethod:POST\r\npath:/webrtc/subscription\r\n\r\n{"endpoint":[{"type":"answerer","connection":"36","topic":["sdp","status"]}],"notify_addr":"endpoint8735"}'''
        b = '''request:2\r\nmethod:PUT\r\npath:/webrtc/push\r\n\r\n{"endpoint":{"type":"offerer","connection":"36"},"message":{"status":"connecting"}}'''
        c = '''request:5\r\nmethod:DELETE\r\npath:/webrtc/subscription\r\n\r\n{"endpoint":[{"type":"answerer","connection":"36","topic":["sdp","status"]}],"notify_addr":"endpoint8735"}'''
        d = '''request:4\r\nmethod:PUT\r\npath:/webrtc/push\r\n\r\n{"endpoint":{"type":"offerer","connection":"52"},"message":{"sdp":{"candidate":"candidate:2811811066 1 udp 2113937151 172.16.121.25 53907 typ host generation 0 ufrag LqLw network-cost 50","sdpMid":"video","sdpMLineIndex":0,"usernameFragment":"LqLw"}}}'''
        wsa.send(a)
        wsa.send(b)
        wsa.send(c)
        arrw = []
        for x in range(0,5):
            arrw.append(wsa.recv())
            print "ws.recv_B%s is %s" % (x,arrw[x])
        wsa.close()

    def Sock_PUT(self,url, port, path, head, body):
        ws = create_connection("ws://172.16.120.22:8181/endpoint5212")
        re = ws.send("{\"endpoint\":{\"type\":\"offerer\",\"connection\":\"208\"},\"message\":{\"status\":\"connected\"}}")
        print ws.recv()
        #print ws.status
        #print ws.recv_data()
        self.logobj.debug("WebSocket_Project End")
        self.logobj.debug("WebSocket_main End")
        ws.close()
    # def Sock_DELETE(self,url, port, path, head, body):
    #     ws = create_connection("ws://172.16.120.22:8181/endpoint5212")
    #     re = ws.send("{\"endpoint\":{\"type\":\"offerer\",\"connection\":\"208\"},\"message\":{\"status\":\"connected\"}}")
    #     print ws.recv()
    #     #print ws.status
    #     #print ws.recv_data()
    #     self.logobj.debug("WebSocket_Project End")
    #     self.logobj.debug("WebSocket_main End")
    #     ws.close()


if __name__ == "__main__":
    ws = WebSocket_Project("test")
    #ws.Sock_POST(1,2,3,4)
    ws.Sock_DELETE(1,2,3,5,5)