#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Fuction.logging_class import Logger
from Fuction.file_con import GetDir,MkdirFolder
import os
import datetime

class Main():
    def __init__(self):
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H')
        path = os.getcwd() + r'\Logs'+'\\'+time+r'\main_frame.log'
        self.logobj = Logger(path)

    def St_Test(self):
        '''执行测试用例py脚本'''
        self.logobj.debug("GetDir Begin")
        path_py = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/venv/Scripts/python.exe"
        self.logobj.debug("GetDir End")
        for x in GetDir(os.getcwd()+r'/Test_cases/new_test/'):
            self.logobj.debug( x["TEST"]+" Begin")
            os.system(path_py+" "+x["TEST"])
            self.logobj.debug(x["TEST"] + " End")
        #self.logobj.debug(GetDir(os.getcwd()+r'/Test_cases'))

MkdirFolder()
main = Main()
main.St_Test()