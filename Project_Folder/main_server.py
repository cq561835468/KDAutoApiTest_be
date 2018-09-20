#coding=utf-8
from flask import Flask
import json
from main_frame import Main

app = Flask(__name__)

@app.route('/test/')
def hello_world():
    #Main().St_Test('VIID')
    s=[u'张三',u'年龄',u'姓名']
    t={}
    t['data']=s
    return json.dumps(t,ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0')