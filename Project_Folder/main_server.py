#coding=utf-8
from flask import Flask, request
from flask import jsonify

import json
from main_frame import Main
from Fuction.Web_Api import Web_Api

app = Flask(__name__)

@app.route('/FILE_Content/', methods=['GET'])
def FILE_Content():
    '''pre判断'''
    print request.url
    urlsp = request.url.split('?')
    if urlsp[1] == "undefined":
        return '''<pre></pre>'''

    with open(urlsp[1]) as f:
        a = f.read()
    return a
@app.route('/FILE/', methods=['POST'])
def FILE():
    #Main().St_Test('VIID')
    if not request.form:
        print "ok"
        return '''<pre></pre>'''
    print request.form['ORG_NAME']
    with open(request.form['ORG_NAME']) as f:
        a = f.read()
    return a

@app.route('/GTC/')
def Get_Foled():
    WA = Web_Api()
    LS = WA.GetTestCase()
    return jsonify(LS)

if __name__ == '__main__':
    app.run(host='0.0.0.0')