#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#*******************************
# Auther:chenqi
# Function:网站对外API接口
#*******************************

import os,pathlib

class Web_Api():
    def __init__(self):
        pass

    def pId_id_P(self,num):
        '''id计算'''
        nums = num * 10+1
        return nums

    def Get_pId_id_Nroot(self,list,name):
        '''输入List_Nodes 输出根据List_Nodes算出的ID'''
        for x in list:
            if x["name"] == name:
                return [self.pId_id_P(x["id"]),self.pId_id_P(x["pId"])]
        return 0

    def Get_IPN_Folder(self, list, num, x):
        '''目录字典'''
        id = list["id"] * 10 + num
        pId = list["id"]
        list = {"id": id, "pId": pId, "name": x, "isParent":"true"}
        return list

    def Get_IPN_File(self, list, num, x, folder):
        '''文件字典'''
        id = list["id"] * 10 + num
        pId = list["id"]
        list = {"id": id, "pId": pId, "name": x, "path": folder, "isParent":"false"}
        return list

    def GetTestCase(self,folder=os.getcwd()+"\\"+"Test_cases"):
        '''获取测试用例目录nodejs'''
        List_Nodes=[{"id":1, "pId":0, "name":"Test_cases"}]
        for root, dirs, files in os.walk(folder):
            numl = 1
            if str(pathlib.Path(root).parent) == os.getcwd():
                '''根目录特殊处理'''
                for x in dirs:
                    list = self.Get_IPN_Folder(List_Nodes[0], numl, x)
                    numl +=1
                    List_Nodes.append(list)
                for x in files:
                    list = self.Get_IPN_File(List_Nodes[0], numl, x, root+"\\"+x)
                    numl +=1
                    List_Nodes.append(list)
            else:
                '''常规处理'''
                for x in dirs:
                    lists_name = [no_xx for no_xx in List_Nodes if no_xx["name"] == pathlib.Path(root).name]
                    list = self.Get_IPN_Folder(lists_name[0], numl, x)
                    numl += 1
                    List_Nodes.append(list)
                for x in files:
                    lists_name = [no_xx for no_xx in List_Nodes if no_xx["name"] == pathlib.Path(root).name]
                    list = self.Get_IPN_File(lists_name[0], numl, x, root+"\\"+x)
                    numl +=1
                    List_Nodes.append(list)

        print List_Nodes
        return List_Nodes




if __name__ =="__main__":
    wa = Web_Api()
    wa.GetTestCase("../Test_cases")