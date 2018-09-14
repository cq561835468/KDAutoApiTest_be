#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import os,json
class CreateHtml():
    def __init__(self):
        if os.path.exists(os.getcwd() +r'\Report_Html\report_project.html'):
            os.remove(os.getcwd() +r'\Report_Html\report_project.html')
        self.soup_Conf = BeautifulSoup(open(os.getcwd() + r'\Fuction\report.html'), 'lxml')

    def Read_JsonData(self,file):
        with open(file, 'r') as load_f:
            load_dict = json.load(load_f)
        return load_dict

    def Write_Html(self):
        sa = open(os.getcwd() +r'\Report_Html\report_project.html','w')
        sa.write(str(self.soup_Conf))
        sa.close()

    def Insert_table(self, tables, values):
        '''插入第一张表'''
        for x in values:
            print x
            print values[x]
            tr = self.soup_Conf.new_tag('tr')
            data = self.soup_Conf.new_tag('td')
            data2 = self.soup_Conf.new_tag('td')
            tr.insert(0, data)
            tr.insert(1, data2)
            tables.append(tr)
            data.string = x
            data2.string = values[x]

    def Insert_table_S(self, table, values):
        '''插入第一张表'''
        list_all_table2 = []
        list_all_table2.append(values["product"]) #产品名称
        list_all_table2.append(values["module"])  # 产品模块
        list_all_table2.append(values["method"])  # 产品方法
        list_all_table2.append(values["TestListName"])  # 产品用例集
        list_all_table2.append(values["iter"])  # 产品用例集迭代次数
        for x in values:
            tr = self.soup_Conf.new_tag('tr')
            data = self.soup_Conf.new_tag('td')
            data2 = self.soup_Conf.new_tag('td')
            tr.insert(0, data)
            tr.insert(1, data2)
            tables.append(tr)
            data.string = x
            data2.string = values[x]

    def run(self,filelist,runtime,time):
        table = self.soup_Conf('table')
        Re_JsonData = self.Read_JsonData(filelist[0])
        print Re_JsonData["product"]
        self.Insert_table(table[0], {u"执行时间": time})
        self.Insert_table(table[0], {u"产品名称": Re_JsonData["product"]})
        self.Insert_table(table[0], {u"框架版本": "V1.1"})
        #self.Insert_table(table[0],{u"执行时间":time})
        for x in filelist:
            Re_JsonData = self.Read_JsonData(x)
            print Re_JsonData
            self.Insert_table_S(table,Re_JsonData)
        self.Write_Html()
        #table1 = self.soup_Conf('table')
        #self.Insert_table()
        #print len(table1)
        #print "hello world"