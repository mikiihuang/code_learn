__author__ = 'yumihuang'
# project name:codelearn
# time:2020-07-29

from flask import Flask,render_template

#使用方法：在浏览器中输入的url为http://127.0.0.1:5000/1/时，显示已登陆的用户名和年龄，以及退出按钮；
# 当在浏览器输出的url后面不是1时，显示登陆和注册

app = Flask("__name__")
@app.route("/<is_login>/")
def login(is_login):
    if is_login == '1':
        user = {"name":"Yumi","age":24}
        return render_template("login_check.html",user=user)
    else:
        return render_template("login_check.html")
if __name__ == '__main__':
    app.run(debug=True)