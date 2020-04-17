__author__ = 'yumihuang'
# project name:codelearn
# time:2020-04-02
#






###############本代码是瞎写时候的测试代码###############




# import numpy as np
# import math
# import matplotlib.pyplot as plt
# x=np.arange(0,8,0.05)
# y1=[]
# y2=[]
# for a in x:
#     try:
#         y1.append(2*math.log(a+1,3))
#
#     except:
#         y1.append(0)
# for b in y1:
#     y2.append((1.2+1)*b/(1.2+b))
# plt.xlim((0,8))
# plt.ylim((0,4))
# ax = plt.gca()
# #把上面和右面的轴设置为消失
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# #设置下面的线为x轴，左边的线为y轴
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# #x轴的position放在y轴的0点上
# ax.spines['bottom'].set_position(('data',-0))# outward,axes
# ax.spines['left'].set_position(('data',0))
#
# plot1=plt.plot(x,y1,'-g',linestyle='--',label='TF score')
#
#
# plot2=plt.plot(x,y2,'-r',label='BM25 TF score')
#
# plt.xlabel(u"Term Frequency")
# plt.ylabel(u"TF Score")
# plt.legend()
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
#
# #figure就是一个大窗口
# x = np.linspace(-3,3,50)
# y1 = 2*x+1
# y2 = x**2
#
# plt.figure()
# plt.plot(x,y2)
# #figure plot第二条线,红色虚线
# plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
# #x limit和y limit
# plt.xlim((-1,2))
# plt.ylim((-2,3))
# plt.xlabel('I am x')
# plt.ylabel('I am y')
# #设置坐标轴的单位小标
# # new_ticks = np.linspace(-1,2,5)
# # plt.xticks(new_ticks)
# #坐标轴小标换成文字
# plt.yticks([-2,-1.8,-1,1.23,3],['really bad','bad','normal','good','really good'])
#
# #gca = 'get current axis'
#
# plt.legend(loc='lower right')
# plt.show()

# g_b = 3
# def t1():
#     global g_b
#     while g_b<6:
#         g_b +=1
#         print("now is"+str(g_b))
# t1()
# print(g_b)
# import time
# time_stamp = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
# print(time_stamp)


'''
模拟人人网登录和获取个人主页数据的整个过程
通过cookie管理器，用于状态维持和会话跟踪技术
'''

# 模拟人人网登陆操作
import requests
import gzip
import re,time

ses = requests.Session() # 获取可以维持会话状态的请求对象

# 登录函数
def doLogin():
    login_url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=202035910728"
    data = {
        "email": "18810400465",

        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': '1',
        'captcha_type': 'web_login',
        # 这个加密之后的密码直接复制
        'password': '96a837fc9a233c64b19eac4fd9243be5d00afe86c7b7644ff87515d60e5b5729',
        'rkey': '9ea70e6ffb518d0684c89e05bd78feaa',
        'f': 'http%3A%2F%2Fwww.renren.com%2F969835232',
    }
    resp=ses.post(login_url, data=data)
    print(resp.text)
    print('登录成功!')

# 获取个人数据
def getData():
    # 请求示例：http://www.renren.com/111111111
    req_url = "http://www.renren.com/your-id"
    res = ses.get(req_url)
    html = res.content.decode('utf-8')
    print(re.findall(("<title>(.*?)</title>"), html)) # ['人人网 - 你的名字'] 此处会输出如下信息

if __name__ == "__main__":
    # 登录
    print("登录中...")
    doLogin() # 登录操作
    # 此处用于模拟，应该在回调中实现获取个人数据
    time.sleep(2) # 此处仅作模拟, 延迟2s的时间
    getData() # 获取个人数据
