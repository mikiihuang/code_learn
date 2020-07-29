__author__ = 'yumihuang'
# project name:codelearn
# time:2020-07-29
from flask import  Flask,url_for
app = Flask(__name__)


@app.route("/")
def hello():
    return "this is hello function"

@app.route("/home/<name>")
def get_name(name):
    return "this is %"%name

@app.route("/test")
def test():
    print(url_for('hello'))
    print(url_for('get_name',name="yumi"))
    print(url_for('test'))

if __name__ == '__main__':
    app.run(debug=True)
