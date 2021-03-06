#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Project_Folder.Fuction.logging_class import Logger
from Project_Folder.Fuction.file_con import GetDir,MkdirFolder,GetDir_json,Create_Html_Report
import os
import datetime
import threading

class Auto_API(threading.Thread):
    def __init__(self):
        pass
    def start(self,path_py,filename):
        os.system(path_py + " " + filename)


class Main():
    def __init__(self):
        self.time = datetime.datetime.now().strftime('%Y-%m-%d_%H')
        self.time_lo = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        #endtime = datetime.datetime.now()
        #self.run_time = ((endtime - starttime).microseconds) / 1000
        path = os.getcwd() + r'\Logs'+'\\'+self.time+r'\main_frame.log'
        MkdirFolder(os.getcwd() + r'\Logs' + '\\' + self.time)  # 新建log日志
        MkdirFolder(os.getcwd() + r'\Reports' + '\\' + self.time)  # 新建report
        self.logobj = Logger(path)

    def run_list_thread(self, path_py, arrw):
        AA = Auto_API()
        AA.start(path_py, arrw)

    def St_Test(self,folder=None):
        '''执行测试用例py脚本'''
        self.logobj.debug("GetDir Begin")
        path_py = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/venv/Scripts/python.exe"
        self.logobj.debug("GetDir End")
        if folder:
            path = os.getcwd()+r'/Test_cases/'+folder+'/'
        else:
            path = os.getcwd() + r'/Test_cases/'
        for x in GetDir(path):
            self.logobj.debug( x["TEST"]+" Begin")
            self.run_list_thread(path_py,x["TEST"]) #多线程执行脚本
            self.logobj.debug(x["TEST"] + " End")
        #self.logobj.debug(GetDir(os.getcwd()+r'/Test_cases'))
        time_end = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        Create_Html_Report(GetDir_json("Reports/" + str(self.time)), time_end, self.time_lo)


if __name__ == "__main__":
    main = Main()
    main.St_Test('Demo_Project')