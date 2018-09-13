from bs4 import BeautifulSoup
import os
class CreateHtml():
    def __init__(self):
        if os.path.exists(os.getcwd() +r'\Report_Html\report_project.html'):
            os.remove(os.getcwd() +r'\Report_Html\report_project.html')
    def run(self):

        print "hello world"