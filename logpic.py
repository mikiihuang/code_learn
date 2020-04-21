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

# # 模拟人人网登陆操作
# import requests
# import gzip
# import re,time
#
# ses = requests.Session() # 获取可以维持会话状态的请求对象
#
# # 登录函数
# def doLogin():
#     login_url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=202035910728"
#     data = {
#         "email": "18810400465",
#
#         'origURL': 'http://www.renren.com/home',
#         'domain': 'renren.com',
#         'key_id': '1',
#         'captcha_type': 'web_login',
#         # 这个加密之后的密码直接复制
#         'password': '96a837fc9a233c64b19eac4fd9243be5d00afe86c7b7644ff87515d60e5b5729',
#         'rkey': '9ea70e6ffb518d0684c89e05bd78feaa',
#         'f': 'http%3A%2F%2Fwww.renren.com%2F969835232',
#     }
#     resp=ses.post(login_url, data=data)
#     print(resp.text)
#     print('登录成功!')
#
# # 获取个人数据
# def getData():
#     # 请求示例：http://www.renren.com/111111111
#     req_url = "http://www.renren.com/your-id"
#     res = ses.get(req_url)
#     html = res.content.decode('utf-8')
#     print(re.findall(("<title>(.*?)</title>"), html)) # ['人人网 - 你的名字'] 此处会输出如下信息
#
# if __name__ == "__main__":
#     # 登录
#     print("登录中...")
#     doLogin() # 登录操作
#     # 此处用于模拟，应该在回调中实现获取个人数据
#     time.sleep(2) # 此处仅作模拟, 延迟2s的时间
#     getData() # 获取个人数据
ll = [{'HTTP': 'HTTP://113.194.28.148'}, {'HTTPS': 'HTTPS://223.241.79.119'}, {'HTTP': 'HTTP://121.8.146.99'}, {'HTTP': 'HTTP://113.195.225.225'}, {'HTTPS': 'HTTPS://223.241.116.161'}, {'HTTP': 'HTTP://211.142.169.4'}, {'HTTPS': 'HTTPS://58.56.149.198'}, {'HTTPS': 'HTTPS://117.45.139.84'}, {'HTTP': 'HTTP://111.222.141.127'}, {'HTTP': 'HTTP://115.219.105.229'}, {'HTTPS': 'HTTPS://183.195.106.118'}, {'HTTPS': 'HTTPS://60.31.213.115'}, {'HTTPS': 'HTTPS://117.45.139.249'}, {'HTTPS': 'HTTPS://221.1.200.242'}, {'HTTPS': 'HTTPS://171.35.221.57'}, {'HTTP': 'HTTP://223.100.166.3'}, {'HTTP': 'HTTP://121.237.148.82'}, {'HTTPS': 'HTTPS://122.241.32.63'}, {'HTTPS': 'HTTPS://110.73.41.80'}, {'HTTPS': 'HTTPS://120.79.61.114'}, {'HTTP': 'HTTP://122.241.17.172'}, {'HTTP': 'HTTP://122.241.34.188'}, {'HTTPS': 'HTTPS://222.95.144.23'}, {'HTTPS': 'HTTPS://122.241.32.159'}, {'HTTP': 'HTTP://121.237.148.16'}, {'HTTPS': 'HTTPS://122.14.47.21'}, {'HTTPS': 'HTTPS://223.241.119.244'}, {'HTTPS': 'HTTPS://116.113.27.170'}, {'HTTPS': 'HTTPS://171.35.223.170'}, {'HTTP': 'HTTP://121.237.149.50'}, {'HTTPS': 'HTTPS://144.52.243.32'}, {'HTTPS': 'HTTPS://121.237.149.130'}, {'HTTPS': 'HTTPS://110.243.9.72'}, {'HTTPS': 'HTTPS://110.189.152.86'}, {'HTTP': 'HTTP://113.208.115.190'}, {'HTTPS': 'HTTPS://223.241.117.118'}, {'HTTP': 'HTTP://125.126.122.44'}, {'HTTP': 'HTTP://117.88.176.188'}, {'HTTPS': 'HTTPS://121.237.149.108'}, {'HTTP': 'HTTP://117.88.177.244'}, {'HTTP': 'HTTP://114.104.135.251'}, {'HTTP': 'HTTP://223.241.117.210'}, {'HTTPS': 'HTTPS://125.126.117.30'}, {'HTTPS': 'HTTPS://125.126.109.112'}, {'HTTP': 'HTTP://124.200.36.118'}, {'HTTP': 'HTTP://115.219.105.158'}, {'HTTP': 'HTTP://150.138.106.174'}, {'HTTPS': 'HTTPS://115.219.107.158'}, {'HTTP': 'HTTP://118.114.164.174'}, {'HTTP': 'HTTP://202.107.233.123'}, {'HTTPS': 'HTTPS://125.126.98.137'}, {'HTTPS': 'HTTPS://125.126.107.48'}, {'HTTP': 'HTTP://125.126.114.7'}, {'HTTPS': 'HTTPS://125.126.114.247'}, {'HTTPS': 'HTTPS://111.231.239.143'}, {'HTTPS': 'HTTPS://115.223.64.38'}, {'HTTPS': 'HTTPS://58.254.220.116'}, {'HTTP': 'HTTP://115.223.109.167'}, {'HTTP': 'HTTP://115.223.96.231'}, {'HTTPS': 'HTTPS://171.35.168.113'}, {'HTTP': 'HTTP://114.239.211.175'}, {'HTTP': 'HTTP://27.43.188.66'}, {'HTTPS': 'HTTPS://117.88.4.162'}, {'HTTP': 'HTTP://110.73.47.126'}, {'HTTP': 'HTTP://171.35.173.121'}, {'HTTP': 'HTTP://106.75.177.227'}, {'HTTPS': 'HTTPS://218.75.69.50'}, {'HTTP': 'HTTP://115.223.94.243'}, {'HTTPS': 'HTTPS://124.93.201.59'}, {'HTTP': 'HTTP://222.95.144.181'}, {'HTTP': 'HTTP://222.95.241.80'}, {'HTTP': 'HTTP://223.241.117.132'}, {'HTTP': 'HTTP://117.88.5.19'}, {'HTTPS': 'HTTPS://223.241.116.201'}, {'HTTP': 'HTTP://110.73.0.113'}, {'HTTPS': 'HTTPS://117.88.4.242'}, {'HTTP': 'HTTP://202.115.142.147'}, {'HTTP': 'HTTP://117.88.5.253'}, {'HTTPS': 'HTTPS://115.219.105.8'}, {'HTTPS': 'HTTPS://171.35.170.144'}, {'HTTPS': 'HTTPS://115.219.109.194'}, {'HTTPS': 'HTTPS://120.39.216.129'}, {'HTTPS': 'HTTPS://115.223.68.95'}, {'HTTP': 'HTTP://115.219.104.57'}, {'HTTP': 'HTTP://115.223.88.91'}, {'HTTP': 'HTTP://121.237.149.165'}, {'HTTPS': 'HTTPS://222.95.144.204'}, {'HTTPS': 'HTTPS://121.33.220.158'}, {'HTTPS': 'HTTPS://119.254.94.93'}, {'HTTPS': 'HTTPS://175.148.79.80'}, {'HTTPS': 'HTTPS://115.219.104.254'}, {'HTTP': 'HTTP://121.40.162.239'}, {'HTTP': 'HTTP://117.68.190.162'}, {'HTTPS': 'HTTPS://163.204.244.185'}, {'HTTP': 'HTTP://113.194.31.60'}, {'HTTPS': 'HTTPS://182.92.220.212'}, {'HTTPS': 'HTTPS://117.88.4.160'}, {'HTTPS': 'HTTPS://222.95.144.61'}]
# print(len(ll))
list1 = ['Google', 'Runoob', 'Taobao']
list_pop=list1.pop(-1)
print("删除的项为 :", list_pop)
# print "列表现在为 : ", list1