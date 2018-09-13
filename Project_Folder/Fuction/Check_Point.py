#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from Fuction.file_con import MkdirFolder
from logging_class import Logger
import os
import sys
import datetime
import json
sys.path.append("../../../../")

class CheckPoint():
    def __init__(self,name,Test_list):
        self.Test_list = Test_list
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H')
        self.logobj = Logger(os.getcwd() + r'\Logs' + '\\' + time + '\\' + 'CheckPoint.log')
        folder = name.split('\\')[-4:-1]
        self.folder_tmp = {}
        self.folder_tmp["State"] = "Pass"
        self.folder_tmp["product"] = folder[0]
        self.folder_tmp["module"] = folder[1]
        self.folder_tmp["method"] = folder[2]
        self.folder_tmp["iter"] = len(Test_list)
        dir =  '\\'.join(folder)
        self.path = os.getcwd()+"\Reports"+"\\"+time+"\\"+dir
        self.path_js = self.path+'\\'+name.split('\\')[-1][:-3]+'.json'
        MkdirFolder(self.path)
        file = open(self.path_js,'w')
        file.write(json.dumps(self.folder_tmp))
        file.close()
        self.CreateTestCaseList(Test_list)

    def error(self,filename):
        '''error'''
        with open(self.path_js, 'r') as load_f:
            load_dict = json.load(load_f)
        for x in self.Test_list:
            load_dict[x]["Status"] = 'Error'
        file = open(self.path_js, 'w')
        file.write(json.dumps(load_dict, indent=4))
        file.close()
        self.logobj.debug("%s Error" % filename)
        #print("%s Error" % filename)

    def json_report(self,name,pass_or_fail,testName,target="result"):
        '''json报告写入'''
        with open(self.path_js, 'r') as load_f:
            load_dict = json.load(load_f)
        arrw = {}
        arrw[name] = pass_or_fail
        load_dict[testName][target].append(arrw)
        file = open(self.path_js, 'w')
        file.write(json.dumps(load_dict, indent=4))
        file.close()

    def json_method(self,testName,target,method):
        '''json报告写入'''
        with open(self.path_js, 'r') as load_f:
            load_dict = json.load(load_f)
        load_dict[testName][target] = method
        file = open(self.path_js, 'w')
        file.write(json.dumps(load_dict, indent=4))
        file.close()

    def CreateTestCaseList(self,Test_list):
        '''创建测试用例对应dom树'''
        with open(self.path_js, 'r') as load_f:
            load_dict = json.load(load_f)
        for x in Test_list:
            load_dict[x] = {}
            load_dict[x]["result"] = []
            load_dict[x]["method"] = []
            load_dict[x]["detail"] = []
            load_dict[x]["Response_Time"] = []
            load_dict[x]["Status"] = 'Pass'
        file = open(self.path_js, 'w')
        file.write(json.dumps(load_dict, sort_keys=True, indent=4, separators=(',', ':')))
        file.close()

    def Tests(self,char,name,testname,data1,data2,method,Res_Time):
        '''检查点判断'''
        #self.CreateTestCaseList(testname)
        # if not isinstance(data1,int) and not isinstance(data1,float): #int和float不转码
        #     #data1 = data1.decode("unicode-escape")
        #     data1 = data1.decode("utf-8")
        #     print data1
        Begin_str = u"[CheckPoint]%s[Ori_Data]%s"
        End_str = u"[Expect_Data]%s"
        Pass_str = u"[Pass]"
        Fail_str = u"[Fail]"
        if char == "=":
            if data1 == data2:
                print (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2)
                self.json_report(name, "Pass", testName=testname,target="result")
                self.json_report(name, (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2),
                                 target="detail",testName=testname)
                self.json_method(testname, target="method", method=method)
                self.json_method(testname, target="Response_Time", method=Res_Time)
                return "PASS"
            print (Begin_str+"["+char+"]"+End_str+Fail_str) % (name,data1,data2)
            self.json_report(name, "Fail",target="result",testName=testname)
            self.json_report(name, (Begin_str + "[" + char + "]" + End_str + Fail_str) % (name, data1, data2),target="detail",testName=testname)
            self.json_method(testname, target="method", method=method)
            self.json_method(testname, target="Response_Time", method=Res_Time)
            return "Fail"
        elif char == "<":
            if data1 < data2:
                print (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2)
                self.json_report(name, "Pass", target="result",testName=testname)
                self.json_report(name, (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2), target="detail",testName=testname)
                self.json_method(testname, target="method", method=method)
                self.json_method(testname, target="Response_Time", method=Res_Time)
                return "PASS"
            print (Begin_str+"["+char+"]"+End_str+Fail_str) % (name,data1,data2)
            self.json_report(name, "Fail")
            self.json_report(name, (Begin_str + "[" + char + "]" + End_str + Fail_str) % (name, data1, data2),target="detail",testName=testname)
            self.json_method(testname, target="method", method=method)
            self.json_method(testname, target="Response_Time", method=Res_Time)
            return "Fail"
        elif char == "<="or char == "=<":
            if data1 <= data2:
                print (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2)
                self.json_report(name, "Pass", target="result",testName=testname)
                self.json_report(name, (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2), target="detail",testName=testname)
                self.json_method(testname, target="method", method=method)
                self.json_method(testname, target="Response_Time", method=Res_Time)
                return "PASS"
            print (Begin_str+"["+char+"]"+End_str+Fail_str) % (name,data1,data2)
            self.json_report(name, "Fail", target="result",testName=testname)
            self.json_report(name, (Begin_str + "[" + char + "]" + End_str + Fail_str) % (name, data1, data2),target="detail",testName=testname)
            self.json_method(testname, target="method", method=method)
            self.json_method(testname, target="Response_Time", method=Res_Time)
            return "Fail"
        elif char == ">":
            if data1 > data2:
                print (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2)
                self.json_report(name, "Pass", target="result",testName=testname)
                self.json_report(name, (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2), target="detail",testName=testname)
                self.json_method(testname, target="method", method=method)
                self.json_method(testname, target="Response_Time", method=Res_Time)
                return "PASS"
            print (Begin_str+"["+char+"]"+End_str+Fail_str) % (name,data1,data2)
            self.json_report(name, "Fail", target="result",testName=testname)
            self.json_report(name, (Begin_str + "[" + char + "]" + End_str + Fail_str) % (name, data1, data2),target="detail",testName=testname)
            self.json_method(testname, target="method", method=method)
            self.json_method(testname, target="Response_Time", method=Res_Time)
            return "Fail"
        elif char == ">=" or char == "=>":
            if data1 > data2:
                print (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2)
                self.json_report(name, "Pass", target="result",testName=testname)
                self.json_report(name, (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2), target="detail",testName=testname)
                self.json_method(testname, target="method", method=method)
                self.json_method(testname, target="Response_Time", method=Res_Time)
                return "PASS"
            print (Begin_str+"["+char+"]"+End_str+Fail_str) % (name,data1,data2)
            self.json_report(name, "Fail", target="result",testName=testname)
            self.json_report(name, (Begin_str + "[" + char + "]" + End_str + Fail_str) % (name, data1, data2),target="detail",testName=testname)
            self.json_method(testname, target="method", method=method)
            self.json_method(testname, target="Response_Time", method=Res_Time)
            return "Fail"
        elif char == "!=":
            if data1 != data2:
                print (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2)
                self.json_report(name, "Pass", target="result",testName=testname)
                self.json_report(name, (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2), target="detail",testName=testname)
                self.json_method(testname, target="method", method=method)
                self.json_method(testname, target="Response_Time", method=Res_Time)
                return "PASS"
            print (Begin_str+"["+char+"]"+End_str+Fail_str) % (name,data1,data2)
            self.json_report(name, "Fail", target="result",testName=testname)
            self.json_report(name, (Begin_str + "[" + char + "]" + End_str + Fail_str) % (name, data1, data2),target="detail",testName=testname)
            self.json_method(testname, target="method", method=method)
            return "Fail"
        elif char == "find":
            if data2.find(data1) != -1:
                print (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2)
                self.json_report(name, "Pass", target="result",testName=testname)
                self.json_report(name, (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2), target="detail",testName=testname)
                self.json_method(testname, target="method", method=method)
                self.json_method(testname, target="Response_Time", method=Res_Time)
                return "PASS"
            print (Begin_str+"["+char+"]"+End_str+Fail_str) % (name,data1,data2)
            self.json_report(name, "Fail", target="result",testName=testname)
            self.json_report(name, (Begin_str + "[" + char + "]" + End_str + Fail_str) % (name, data1, data2),target="detail",testName=testname)
            self.json_method(testname, target="method", method=method)
            self.json_method(testname, target="Response_Time", method=Res_Time)
            return "Fail"