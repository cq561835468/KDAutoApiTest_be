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
    def __init__(self,abname,Test_list,iter):
        self.abname = abname.split('\\') #测试用例绝对路径分解
        self.Test_list = Test_list #测试用例名称数组
        self.iter = iter #外部数据组数用于放入迭代
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H')
        dir = '\\'.join(self.abname[-4:-1])
        path = os.getcwd() + "\Reports" + "\\" + time + "\\" + dir #当前保存最新报告路径
        self.json = path+"\\"+self.abname[-1][:-3]+".json"
        self.json_tmp = path+"\\"+self.abname[-1][:-3]+"_tmp.json"
        MkdirFolder(path)
        self.logobj = Logger(os.getcwd() + r'\Logs' + '\\' + time + '\\' + 'CheckPoint.log')
        self.Init_Json_Last("new") #最终

    def Init_Json(self):
        '''新建临时json'''
        self.folder_tmp = {}
        self.folder_tmp["State"] = "Pass"
        self.folder_tmp["product"] = self.abname[-4:-1][0]
        self.folder_tmp["module"] = self.abname[-4:-1][1]
        self.folder_tmp["method"] = self.abname[-4:-1][2]
        self.folder_tmp["TestListName"] = self.abname[-1][:-3]
        self.folder_tmp["iter"] = self.iter
        for x in self.Test_list:
            self.folder_tmp[x] = {}
            self.folder_tmp[x]["result"] = []
            self.folder_tmp[x]["method"] = []
            self.folder_tmp[x]["detail"] = []
            self.folder_tmp[x]["Response_Time"] = []
            self.folder_tmp[x]["Status"] = 'Pass'
        file2 = open(self.json_tmp,'w')
        file2.write(json.dumps(self.folder_tmp, indent=4))
        file2.close()

    def Init_Json_Last(self,key):
        '''最终json操作'''
        if key == "new":
            file1 = open(self.json,'w')
            file1.write("[]")
            file1.close()
        elif key == "append":
            with open(self.json_tmp, 'r') as load_f:
                load_dict_tmp = json.load(load_f)
            with open(self.json, 'r') as load_f:
                load_dict = json.load(load_f)
            load_dict.append(load_dict_tmp)
            os.remove(self.json_tmp)
            file1 = open(self.json,'w')
            file1.write(json.dumps(load_dict, indent=4))
            file1.close()

    def error(self,filename):
        '''error'''
        with open(self.json_tmp, 'r') as load_f:
            load_dict = json.load(load_f)
        for x in self.Test_list:
            load_dict[x]["Status"] = 'Error'
        file = open(self.json_tmp, 'w')
        file.write(json.dumps(load_dict, indent=4))
        file.close()
        self.logobj.debug("%s Error" % filename)
        #print("%s Error" % filename)

    def json_report(self,name,pass_or_fail,testName,target="result"):
        '''json报告第二层写入'''
        with open(self.json_tmp, 'r') as load_f:
            load_dict = json.load(load_f)
        arrw = {}
        arrw[name] = pass_or_fail
        load_dict[testName][target].append(arrw)
        if pass_or_fail == "Fail":
            print "检查点失败"
            load_dict["State"] = "Fail"
        file = open(self.json_tmp, 'w')
        file.write(json.dumps(load_dict, indent=4))
        file.close()

    def json_method(self,testName,target,method):
        '''json报告第一层写入'''
        with open(self.json_tmp, 'r') as load_f:
            load_dict = json.load(load_f)
        load_dict[testName][target] = method
        file = open(self.json_tmp, 'w')
        file.write(json.dumps(load_dict, indent=4))
        file.close()

    def Tests(self,char,name,testname,data1,data2,method,Res_Time):
        '''检查点判断'''
        #    data1 = data1.decode("unicode-escape")
        #    data1 = data1.decode("utf-8")
        Begin_str = u"[CheckPoint]%s[Ori_Data]%s"
        End_str = u"[Expect_Data]%s"
        Pass_str = u"[Pass]"
        Fail_str = u"[Fail]"
        Pass_Long_Str = (Begin_str + "["+char+"]"+End_str+Pass_str) % (name, data1, data2)
        Fail_Long_Str = (Begin_str+"["+char+"]"+End_str+Fail_str) % (name, data1, data2)
        if char == "=":
            if data1 == data2:
                print Pass_Long_Str
                self.json_report(name, "Pass", testName=testname,target="result")
                self.json_report(name, Pass_Long_Str,target="detail",testName=testname)
                self.json_method(testname, target="method", method=method)
                self.json_method(testname, target="Response_Time", method=Res_Time)
                return "PASS"
            print Fail_Long_Str
            self.json_report(name, "Fail",target="result",testName=testname)
            self.json_report(name, Fail_Long_Str,target="detail",testName=testname)
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