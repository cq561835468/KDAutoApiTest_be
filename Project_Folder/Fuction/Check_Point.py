#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class CheckPoint():
    def __init__(self):
        pass
    def Tests(self,char,data1,data2):
        data1 = data1.decode("unicode-escape")
        if char == "=":
            if data1 == data2:
                print u"[CheckPoint]Ori_Data:%s = Expect_Data:%s " % (data1,data2)
        elif char == "<":
            if data1 < data2:
                print u"[CheckPoint]Ori_Data:%s < Expect_Data:%s " % (data1,data2)
        elif char == "<="or char == "=<":
            if data1 <= data2:
                print u"[CheckPoint]Ori_Data:%s <= Expect_Data:%s " % (data1,data2)
        elif char == ">":
            if data1 > data2:
                print u"[CheckPoint]Ori_Data:%s > Expect_Data:%s " % (data1,data2)
        elif char == ">=" or char == "=>":
            if data1 > data2:
                print u"[CheckPoint]Ori_Data:%s => Expect_Data:%s " % (data1,data2)