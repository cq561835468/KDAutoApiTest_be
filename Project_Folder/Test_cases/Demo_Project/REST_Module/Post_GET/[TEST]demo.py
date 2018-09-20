#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys,os,json,time,random,traceback,pprint
sys.path.append("../../../../")
sys.path.append(os.getcwd())
from model.REST.REST_main import REST_Request
from model.WebSocket.WebSocket_main import WebSocket_Request
from Fuction.Check_Point import CheckPoint
class Test_demo:
    def __init__(self):
        global null
        null = ''
        '''测试用例命名'''
        self.Test_Cases_name = ["livestream","sessioninfo","viewer","subscription","push","subscription_delete","viewer_delete"]
        '''外部数据获取'''
        self.file_out = self.Get_Json("[DATA][Demo_Project][REST_Module_GET_POST]demo.json")
        '''实例化'''
        self.CP = CheckPoint(os.path.realpath(__file__), self.Test_Cases_name,len(self.file_out))

    def Get_Json(self,filename):
        '''读取外部数据'''
        with open(os.path.dirname(os.path.realpath(__file__))+"\\"+filename, 'r') as load_f:
            load_dict = json.load(load_f)
        return load_dict

    def Request(self):
        '''参数化执行测试用例'''
        '''包头'''
        try:
            head = {
                "Content-Type": "application/json"
            }
            for x in self.file_out:
                '''包体'''
                self.CP.Init_Json() #每次都数据化临时json报告
                body = {
                    "source": {
                    "type": "rtsp",
                    "options":{
                        "rtsp":{
                            "audioCodec":"pcma",
                            "codec":"h264",
                            "url":str(x["DevID"])
                            }
                        }
                    }
                }
                self.Response_Api = REST_Request(name="[MSS][LiveStream][POST]").run(method=x["method"],
                                                                                     url=x["url"],
                                                                                     port=x["port"],
                                                                                     path=x["path_livestream"],
                                                                                     head=head,
                                                                                     body=json.dumps(eval(json.dumps(body))))
                eva_Response_Api = eval(self.Response_Api.content) #格式转换
                streamId = eva_Response_Api["streamId"]
                body2 = {
                    "connectionId": streamId,
                    "sessionType":"single"
                }
                self.Response_Api2 = REST_Request(name="[MSS][sessionInfo][PUT]").run(method=x["method2"],
                                                                                     url=x["url"],
                                                                                     port=x["port"],
                                                                                     path=x["path_sessionInfo"],
                                                                                     head=head,
                                                                                     body=json.dumps(eval(json.dumps(body2))))
                body3 = {
                    "type":x["type"],
                    "Id":streamId,
                    "video":x["video"],
                    "audio":x["audio"]
                }
                self.Response_Api3 = REST_Request(name="[MSS][viewer][POST]").run(method=x["method"],
                                                                                     url=x["url"],
                                                                                     port=x["port"],
                                                                                     path=x["path_viewer"],
                                                                                     head=head,
                                                                                     body=json.dumps(eval(json.dumps(body3))))
                eva_Response_Api2 = eval(self.Response_Api3.content) #格式转换
                print self.Response_Api3.content
                viewerId = eva_Response_Api2["viewerId"]
                signalingBridge = eva_Response_Api2["signalingBridge"]
                endpoint = random.randint(1,10000)
                ss = signalingBridge.split(':')
                body_socket1 = '''request:1\r\nmethod:POST\r\npath:/webrtc/subscription\r\n\r\n{"endpoint":[{"type":"answerer","connection":"'''+str(viewerId)+'''","topic":["sdp","status"]}],"notify_addr":"endpoint'''+str(endpoint)+'''"}'''
                body_socket2 = '''request:2\r\nmethod:PUT\r\npath:/webrtc/push\r\n\r\n{"endpoint":{"type":"offerer","connection":"''' + str(viewerId) + '''"},"message":{"status":"connecting"}}'''
                body_socket3 = '''request:3\r\nmethod:POST\r\npath:/webrtc/subscription\r\n\r\n{"endpoint":[{"type":"answerer","connection":"'''+str(viewerId)+'''","topic":["sdp","status"]}],"notify_addr":"endpoint'''+str(endpoint)+'''"}'''
                self.Response_Api4 = WebSocket_Request(name="[MSS][subscription][POST]").run(method=x["method4"],
                                                                                     url=ss[0]+':'+ss[1],
                                                                                     port=ss[2],
                                                                                     path="/endpoint"+str(endpoint),
                                                                                     head=head,
                                                                                     body=[body_socket1],
                                                                                     timeout=3)
                self.Response_Api5 = WebSocket_Request(name="[MSS][PUSH][PUT]").run(method=x["method4"],
                                                                                     url=ss[0]+':'+ss[1],
                                                                                     port=ss[2],
                                                                                     path="/endpoint"+str(endpoint),
                                                                                     head=head,
                                                                                     body=[body_socket2],
                                                                                     timeout=3)
                self.Response_Api6 = WebSocket_Request(name="[MSS][subscription][delete]").run(method=x["method4"],
                                                                                     url=ss[0]+':'+ss[1],
                                                                                     port=ss[2],
                                                                                     path="/endpoint"+str(endpoint),
                                                                                     head=head,
                                                                                     body=[body_socket3],
                                                                                     timeout=3)
                pprint.pprint(self.Response_Api4)
                body6 = {"viewerId": str(viewerId), "streamId": streamId}
                self.Response_Api7 = REST_Request(name="[MSS][viewer][POST]").run(method=x["method3"],
                                                                                     url=x["url"],
                                                                                     port=x["port"],
                                                                                     path=x["path_viewer"],
                                                                                     head=head,
                                                                                     body=json.dumps(eval(json.dumps(body6))))

                self.Response_Va(self.Response_Api,x,Test_name=self.Test_Cases_name[0], #用例名称1
                                 method=x["method"], #请求
                                 Res_Time=self.Response_Api.elapsed.microseconds /1000)
                self.CP.Init_Json_Last("append") #将完成的json报告增加到最终报告中
        except Exception, e:
            print 'traceback.format_exc():\n%s' % traceback.format_exc()
            self.CP.Init_Json()
            self.CP.error(os.path.realpath(__file__))
            self.CP.Init_Json_Last("append")
    def Response_Va(self,response,para,Test_name,method,Res_Time):
        '''检查点'''
        self.CP.Tests("=", "Status_code",Test_name,self.Response_Api.status_code, para["Re_State"],method,Res_Time,self.Response_Api.status_code)

demo = Test_demo().Request()

