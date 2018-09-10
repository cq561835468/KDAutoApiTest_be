#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class CheckPoint():
    def __init__(self):
        pass
    def Tests(self,char,name,data1,data2):
        '''检查点判断'''
        data1 = data1.decode("unicode-escape")
        Begin_str = u"[CheckPoint]%s[Ori_Data]%s"
        End_str = u"[Expect_Data]%s"
        Pass_str = u"\033[1;34m [Pass] \033[0m"
        Fail_str = u"\033[1;31m [Fail] \033[0m"
        if char == "=":
            if data1 == data2:
                print (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2)
                return "PASS"
            print (Begin_str+"["+char+"]"+End_str+Fail_str) % (name,data1,data2)
            return "Fail"
        elif char == "<":
            if data1 < data2:
                print (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2)
                return "PASS"
            print (Begin_str+"["+char+"]"+End_str+Fail_str) % (name,data1,data2)
            return "Fail"
        elif char == "<="or char == "=<":
            if data1 <= data2:
                print (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2)
                return "PASS"
            print (Begin_str+"["+char+"]"+End_str+Fail_str) % (name,data1,data2)
            return "Fail"
        elif char == ">":
            if data1 > data2:
                print (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2)
                return "PASS"
            print (Begin_str+"["+char+"]"+End_str+Fail_str) % (name,data1,data2)
            return "Fail"
        elif char == ">=" or char == "=>":
            if data1 > data2:
                print (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2)
                return "PASS"
            print (Begin_str+"["+char+"]"+End_str+Fail_str) % (name,data1,data2)
            return "Fail"
        elif char == "!=":
            if data1 != data2:
                print (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2)
                return "PASS"
            print (Begin_str+"["+char+"]"+End_str+Fail_str) % (name,data1,data2)
            return "Fail"
        elif char == "find":
            if data2.find(data1) != -1:
                print (Begin_str+"["+char+"]"+End_str+Pass_str) % (name,data1,data2)
                return "PASS"
            print (Begin_str+"["+char+"]"+End_str+Fail_str) % (name,data1,data2)
            return "Fail"