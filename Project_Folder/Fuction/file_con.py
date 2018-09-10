#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import datetime

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

def MkdirFolder():
    '''新建日志存放文件夹，按照小时为单位'''
    time = datetime.datetime.now().strftime('%Y-%m-%d_%H')
    if not os.path.exists(os.getcwd() + r'\Logs' + '\\' + time):
        os.mkdir(os.getcwd() + r'\Logs' + '\\' + time)

if __name__ == "__main__":
    print GetDir(os.path.dirname(os.path.dirname(__file__))+r'/Test_cases')