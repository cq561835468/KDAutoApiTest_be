from flask import Flask
from main_frame import Main

app = Flask(__name__)

@app.route('/test/')
def hello_world():
    Main().St_Test('VIID')
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')