#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from Fuction.CreateHtml import CreateHtml

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

def GetDir_json(path):
    '''获取该设备所有用例+外部数据，以数组形式返回'''
    return_list = []
    for root, dirs, files in os.walk(path):
        for x in files:
            if "json" in x:
                return_list.append(root+"\\"+x)
    return return_list

def Create_Html_Report(filelist,run_time,time):
    CreateHtml().run(filelist,run_time,time)

def MkdirFolder(filename):
    '''新建日志存放文件夹，按照小时为单位'''
   #time = datetime.datetime.now().strftime('%Y-%m-%d_%H')
    if not os.path.exists(filename):
        os.makedirs(filename)

if __name__ == "__main__":
    print GetDir(os.path.dirname(os.path.dirname(__file__))+r'/Test_cases')