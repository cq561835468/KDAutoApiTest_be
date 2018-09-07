#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

def GetDir(path):
    '''获取该设备所有用例+外部数据，以数组形式返回'''
    return_list = []
    for root, dirs, files in os.walk(path):
        tmp_list = {}
        for x in files:
            if "[TEST]" in x:
                tmp_list["TEST"] = root+"\\"+x
            if "[DATA]" in x:
                tmp_list["DATA"] = root+"\\"+x
        if tmp_list:
            return_list.append(tmp_list)
    return return_list

def Para_run(dict):
    '''外部数据导入执行python脚本'''
    pass

if __name__ == "__main__":
    print GetDir(os.path.dirname(os.path.dirname(__file__))+r'/Test_cases')