#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import os,json,pprint
class CreateHtml():
    def __init__(self):
        if os.path.exists(os.getcwd() +r'\Report_Html\report_project.html'):
            os.remove(os.getcwd() +r'\Report_Html\report_project.html')
        self.soup_Conf = BeautifulSoup(open(os.getcwd() + r'\Fuction\report.html'), 'lxml')
        self.soup_Conf_detail = BeautifulSoup(open(os.getcwd() + r'\Fuction\report_detail.html'), 'lxml')
        self.ClearFile(os.getcwd() +r'\Report_Html')

    def ClearFile(self,path):
        list_dir = []
        for i in os.listdir(path):
            os.remove(path+"\\"+i)

    def Read_JsonData(self,file):
        with open(file, 'r') as load_f:
            load_dict = json.load(load_f)
        return load_dict

    def Write_Html(self,path,context):
        sa = open(os.getcwd() +path,'w')
        sa.write(str(context))
        sa.close()

    def Json_ALL_Error(self,list,key):
        '''检查用例集、用例失败和总的'''
        num = 0
        if list[key] !="Pass":
            num +=1
        return [1,num]

    def Json_Check_Error(self,list):
        '''检查检查点失败和总的'''
        all,num = 0,0
        for x in list:
            for xx in x:
                if x[xx] !="Pass":
                    all +=1
                    num +=1
                else:
                    all +=1
        return [all,num]

    def Insert_table(self, tables, values):
        '''插入第一张表'''
        for x in values:
            tr = self.soup_Conf.new_tag('tr')
            data = self.soup_Conf.new_tag('td')
            data2 = self.soup_Conf.new_tag('td')
            tr.insert(0, data)
            tr.insert(1, data2)
            tables.append(tr)
            data.string = x
            data2.string = values[x]

    def Insert_table_S(self, table, values):
        '''插入第二张表'''
        Iter_Scal_all,Iter_Scal_error = 0,0
        Tests_All_Scal, Tests_Error_Scal = 0, 0
        Check_All_Scal, Check_Error_Scal = 0, 0
        last = []
        for xx in values:
            try:
                a = self.Json_ALL_Error(xx, "State")
                Iter_Scal_all += a[0]
                Iter_Scal_error += a[1]
                for sa in ["product", "module", "method", "TestListName", "iter"]:
                    '''循环删除'''
                    last.append(xx[sa])
                    del xx[sa]
                if xx["State"] == "Error":
                    print "html error"
                    raise Exception("Test Cases Error")
                del xx["State"]
                for x1 in xx:
                    a1 = self.Json_ALL_Error(xx[x1], "Status")
                    Tests_All_Scal += a1[0]
                    Tests_Error_Scal += a1[1]
                    a2 = self.Json_Check_Error(xx[x1]["result"])
                    Check_All_Scal += a2[0]
                    Check_Error_Scal += a2[1]
                    '''处理数据'''
                    Tests_List = last[0:4]
                    for x in [str(Iter_Scal_all), str(Iter_Scal_error), str(Tests_All_Scal), str(Tests_Error_Scal),
                              str(Check_All_Scal), str(Check_Error_Scal)]:
                        Tests_List.append(x)
            except Exception,e:
                # print "Insert_table_S Error"
                print Exception,e
                # print 'str(e):\t\t', str(e)
                # print 'repr(e):\t', repr(e)
                # print 'e.message:\t', e.message
                Tests_List = last[0:4]
                for x in [str(Iter_Scal_all), str(Iter_Scal_error), str(Tests_All_Scal), str(Tests_Error_Scal),
                          str(Check_All_Scal), str(Check_Error_Scal)]:
                    Tests_List.append("error")
            finally:
                tr = self.soup_Conf.new_tag('tr')
                print Tests_List
                for num,x in enumerate(Tests_List):
                    data = self.soup_Conf.new_tag('td')
                    table.append(tr)
                    tr.insert(num, data)
                    data.string = str(x)
                self.Write_Html(r'\Report_Html\report_project1.html',self.soup_Conf)

    def Insert_Table_Detail(self, table, values, filename):
        '''插入'''
        try:
            last = []
            for xx in values:
                tmp = []
                a = self.Json_ALL_Error(xx, "State")
                for sa in ["product", "module", "method", "TestListName", "iter"]:
                    '''循环删除'''
                    tmp.append(xx[sa])
                    del xx[sa]
                if xx["State"] == "Error":
                    print "html error"
                    raise Exception("Test Cases Error")
                del xx["State"]
                for x1 in xx:
                    a = tmp[0:4]
                    a.append(x1)
                    for xa in xx[x1]["result"]:
                        sa = a[:]
                        sa.append(xa.keys()[0])
                        sa.append(xa[xa.keys()[0]])
                        sa.append(xx[x1]["method"])
                        sa.append(xx[x1]["Response_Time"])
                        sa.append(xx[x1]["Response_State"])
                        last.append(sa)
        except Exception,e:
            print Exception,e
            print 'str(Exception):\t', str(Exception)
            print 'str(e):\t\t', str(e)
            print 'repr(e):\t', repr(e)
            print 'e.message:\t', e.message
            ss = tmp[0:4]
            for x in range(0,6):
                ss.append("Error")
            last.append(ss)
        finally:
            for xap in last:
                tr = self.soup_Conf.new_tag('tr')
                for num, x in enumerate(xap):
                    data = self.soup_Conf.new_tag('td')
                    table.append(tr)
                    tr.insert(num, data)
                    data.string = str(x)
            self.Write_Html(r"\Report_Html" + "\\" + filename + ".html", self.soup_Conf_detail)

    def Insert_head_table(self, table, time, Re_JsonData, runtime):
        self.Insert_table(table, {u"开始时间": time})
        self.Insert_table(table, {u"结束时间": runtime})
        self.Insert_table(table, {u"产品名称": Re_JsonData[0]["product"]})
        self.Insert_table(table, {u"框架版本": "V1.1"})



    def run(self,filelist,endtime,begin_time):
        table = self.soup_Conf('table')
        table_datail = self.soup_Conf_detail('table')
        Re_JsonData = self.Read_JsonData(filelist[0])
        print Re_JsonData
        self.Insert_head_table(table[0], begin_time, Re_JsonData, endtime)
        self.Insert_head_table(table_datail[0], begin_time, Re_JsonData, endtime)
        for x in filelist:
            '''处理汇总'''
            Re_JsonData = self.Read_JsonData(x)
            self.Insert_table_S(table[1],Re_JsonData)
        for xx in filelist:
            '''处理单个详情'''
            filename = os.path.basename(xx)
            Re_JsonData = self.Read_JsonData(xx)
            self.Insert_Table_Detail(table_datail[1],Re_JsonData,filename)
