__author__ = 'yumihuang'
# project name:codelearn
# time:2020-04-02
#
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

g_b = 3
def t1():
    global g_b
    while g_b<6:
        g_b +=1
        print("now is"+str(g_b))
t1()
print(g_b)