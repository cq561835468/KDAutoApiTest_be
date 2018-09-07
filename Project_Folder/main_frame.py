#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Fuction.logging_class import Logger
from Fuction.file_con import GetDir
import os

path = os.getcwd()+r'\Logs\main_frame.logs'
logobj = Logger(path)

def St_Test():
    '''执行测试用例py脚本'''
    logobj.debug("GetDir begin")
    for x in GetDir(os.getcwd()+r'/Test_cases'):
        logobj.debug( x["TEST"]+" begin")
        os.system(x["TEST"]+"")
    logobj.debug(GetDir(os.getcwd()+r'/Test_cases'))
    logobj.debug("GetDir end")

St_Test()