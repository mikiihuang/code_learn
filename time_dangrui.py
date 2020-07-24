__author__ = 'yumihuang'
# project name:codelearn
# time:2020-06-22
import re
import xlwt
#
with open("tpch-benchmark-olap-20200619112632-天翼.log",encoding='utf-8') as f:
    contents = f.readlines()
    RealTimeList = []
    for i in contents:

        try:
            if re.match('real	',i):
                RealTimeList.append(i.replace("real	",'').replace("\n",''))

        except:
            pass


        # if re.match('user	',i):
        #     line.append(i.replace("user	",''))
        # if re.match("sys	",i):
        #     line.append(i.replace("sys	",''))
    userTimeList=[]
    for i in contents:

        try:
            if re.match('user	',i):
                userTimeList.append(i.replace("user	",'').replace("\n",''))

        except:
            pass

    sysTimeList = []
    for i in contents:

        try:
            if re.match('sys	', i):
                sysTimeList.append(i.replace("sys	", '').replace("\n", ''))

        except:
            pass
    assert len(RealTimeList) == len(userTimeList)
    assert len(userTimeList)==len(sysTimeList)


    for a in RealTimeList:
        print(a)