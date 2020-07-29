__author__ = 'yumihuang'
# project name:codelearn
# time:2020-07-29

from flask import Flask,render_template

user = [
   {'name':"Yumi","age":12},
   {'name':"Miki","age":14},
   {"name":"roy","age":24}
]
app = Flask(__name__)
@app.route('/hello/')
def hello_name():
   return render_template('index.html', users =user)


if __name__ == '__main__':

   app.run(debug = True)