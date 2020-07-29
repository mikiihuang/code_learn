__author__ = 'yumihuang'
# project name:codelearn
# time:2020-07-28
from flask import Flask,redirect,url_for,request
app = Flask(__name__)

@app.route("/go")
def hello_world(name):
    return 'Hello %s,welcome!!'%name

@app.route('/login',methods = ['POST','GET'])
def to_which():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for('hello_world',name=user))
    else:
        user = request.args.get("name")
        return redirect(url_for("hello_world",name = user))
if __name__ == '__main__':

    app.run(debug=True)