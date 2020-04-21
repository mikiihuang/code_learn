__author__ = 'yumihuang'
# project name:codelearn
# time:2020-04-20

import requests
from bs4 import BeautifulSoup
import re
import os

######为什么代理ip没用呢。。。####
proxy = [
{'HTTP': 'HTTP://113.194.28.148'},{'HTTPS': 'HTTPS://223.241.79.119'},{'HTTP': 'HTTP://121.8.146.99'},{'HTTP': 'HTTP://113.195.225.225'},{'HTTPS': 'HTTPS://223.241.116.161'},{'HTTP': 'HTTP://211.142.169.4'},{'HTTPS': 'HTTPS://58.56.149.198'},{'HTTPS': 'HTTPS://117.45.139.84'},{'HTTP': 'HTTP://111.222.141.127'},{'HTTP': 'HTTP://115.219.105.229'},{'HTTPS': 'HTTPS://183.195.106.118'},{'HTTPS': 'HTTPS://60.31.213.115'},{'HTTPS': 'HTTPS://117.45.139.249'},{'HTTPS': 'HTTPS://221.1.200.242'},{'HTTPS': 'HTTPS://171.35.221.57'},{'HTTP': 'HTTP://223.100.166.3'},{'HTTP': 'HTTP://121.237.148.82'},{'HTTPS': 'HTTPS://122.241.32.63'},{'HTTPS': 'HTTPS://110.73.41.80'},{'HTTPS': 'HTTPS://120.79.61.114'},{'HTTP': 'HTTP://122.241.17.172'},{'HTTP': 'HTTP://122.241.34.188'},{'HTTPS': 'HTTPS://222.95.144.23'},{'HTTPS': 'HTTPS://122.241.32.159'},{'HTTP': 'HTTP://121.237.148.16'},{'HTTPS': 'HTTPS://122.14.47.21'},{'HTTPS': 'HTTPS://223.241.119.244'},{'HTTPS': 'HTTPS://116.113.27.170'},{'HTTPS': 'HTTPS://171.35.223.170'},{'HTTP': 'HTTP://121.237.149.50'},{'HTTPS': 'HTTPS://144.52.243.32'},{'HTTPS': 'HTTPS://121.237.149.130'},{'HTTPS': 'HTTPS://110.243.9.72'},{'HTTPS': 'HTTPS://110.189.152.86'},{'HTTP': 'HTTP://113.208.115.190'},{'HTTPS': 'HTTPS://223.241.117.118'},{'HTTP': 'HTTP://125.126.122.44'},{'HTTP': 'HTTP://117.88.176.188'},{'HTTPS': 'HTTPS://121.237.149.108'},{'HTTP': 'HTTP://117.88.177.244'},{'HTTP': 'HTTP://114.104.135.251'},{'HTTP': 'HTTP://223.241.117.210'},{'HTTPS': 'HTTPS://125.126.117.30'},{'HTTPS': 'HTTPS://125.126.109.112'},{'HTTP': 'HTTP://124.200.36.118'},{'HTTP': 'HTTP://115.219.105.158'},{'HTTP': 'HTTP://150.138.106.174'},{'HTTPS': 'HTTPS://115.219.107.158'},{'HTTP': 'HTTP://118.114.164.174'},{'HTTP': 'HTTP://202.107.233.123'},{'HTTPS': 'HTTPS://125.126.98.137'},{'HTTPS': 'HTTPS://125.126.107.48'},{'HTTP': 'HTTP://125.126.114.7'},{'HTTPS': 'HTTPS://125.126.114.247'},{'HTTPS': 'HTTPS://111.231.239.143'},{'HTTPS': 'HTTPS://115.223.64.38'},{'HTTPS': 'HTTPS://58.254.220.116'},{'HTTP': 'HTTP://115.223.109.167'},{'HTTP': 'HTTP://115.223.96.231'},{'HTTPS': 'HTTPS://171.35.168.113'},{'HTTP': 'HTTP://114.239.211.175'},{'HTTP': 'HTTP://27.43.188.66'},{'HTTPS': 'HTTPS://117.88.4.162'},{'HTTP': 'HTTP://110.73.47.126'},{'HTTP': 'HTTP://171.35.173.121'},{'HTTP': 'HTTP://106.75.177.227'},{'HTTPS': 'HTTPS://218.75.69.50'},{'HTTP': 'HTTP://115.223.94.243'},{'HTTPS': 'HTTPS://124.93.201.59'},{'HTTP': 'HTTP://222.95.144.181'},{'HTTP': 'HTTP://222.95.241.80'},{'HTTP': 'HTTP://223.241.117.132'},{'HTTP': 'HTTP://117.88.5.19'},{'HTTPS': 'HTTPS://223.241.116.201'},{'HTTP': 'HTTP://110.73.0.113'},{'HTTPS': 'HTTPS://117.88.4.242'},{'HTTP': 'HTTP://202.115.142.147'},{'HTTP': 'HTTP://117.88.5.253'},{'HTTPS': 'HTTPS://115.219.105.8'},{'HTTPS': 'HTTPS://171.35.170.144'},{'HTTPS': 'HTTPS://115.219.109.194'},{'HTTPS': 'HTTPS://120.39.216.129'},{'HTTPS': 'HTTPS://115.223.68.95'},{'HTTP': 'HTTP://115.219.104.57'},{'HTTP': 'HTTP://115.223.88.91'},{'HTTP': 'HTTP://121.237.149.165'},{'HTTPS': 'HTTPS://222.95.144.204'},{'HTTPS': 'HTTPS://121.33.220.158'},{'HTTPS': 'HTTPS://119.254.94.93'},{'HTTPS': 'HTTPS://175.148.79.80'},{'HTTPS': 'HTTPS://115.219.104.254'},{'HTTP': 'HTTP://121.40.162.239'},{'HTTP': 'HTTP://117.68.190.162'},{'HTTPS': 'HTTPS://163.204.244.185'},{'HTTP': 'HTTP://113.194.31.60'},{'HTTPS': 'HTTPS://182.92.220.212'},{'HTTPS': 'HTTPS://117.88.4.160'},{'HTTPS': 'HTTPS://222.95.144.61'},
{'HTTP': 'HTTP://122.234.168.250'},{'HTTP': 'HTTP://113.194.28.148'},{'HTTPS': 'HTTPS://223.241.79.119'},{'HTTP': 'HTTP://121.8.146.99'},{'HTTP': 'HTTP://113.195.225.225'},{'HTTPS': 'HTTPS://223.241.116.161'},{'HTTP': 'HTTP://211.142.169.4'},{'HTTPS': 'HTTPS://58.56.149.198'},{'HTTPS': 'HTTPS://117.45.139.84'},{'HTTP': 'HTTP://111.222.141.127'},{'HTTP': 'HTTP://115.219.105.229'},{'HTTPS': 'HTTPS://183.195.106.118'},{'HTTPS': 'HTTPS://60.31.213.115'},{'HTTPS': 'HTTPS://117.45.139.249'},{'HTTPS': 'HTTPS://221.1.200.242'},{'HTTPS': 'HTTPS://171.35.221.57'},{'HTTP': 'HTTP://223.100.166.3'},{'HTTP': 'HTTP://121.237.148.82'},{'HTTPS': 'HTTPS://122.241.32.63'},{'HTTPS': 'HTTPS://110.73.41.80'},{'HTTPS': 'HTTPS://120.79.61.114'},{'HTTP': 'HTTP://122.241.17.172'},{'HTTP': 'HTTP://122.241.34.188'},{'HTTPS': 'HTTPS://222.95.144.23'},{'HTTPS': 'HTTPS://122.241.32.159'},{'HTTP': 'HTTP://121.237.148.16'},{'HTTPS': 'HTTPS://122.14.47.21'},{'HTTPS': 'HTTPS://223.241.119.244'},{'HTTPS': 'HTTPS://116.113.27.170'},{'HTTPS': 'HTTPS://171.35.223.170'},{'HTTP': 'HTTP://121.237.149.50'},{'HTTPS': 'HTTPS://144.52.243.32'},{'HTTPS': 'HTTPS://121.237.149.130'},{'HTTPS': 'HTTPS://110.243.9.72'},{'HTTPS': 'HTTPS://110.189.152.86'},{'HTTP': 'HTTP://113.208.115.190'},{'HTTPS': 'HTTPS://223.241.117.118'},{'HTTP': 'HTTP://125.126.122.44'},{'HTTP': 'HTTP://117.88.176.188'},{'HTTPS': 'HTTPS://121.237.149.108'},{'HTTP': 'HTTP://117.88.177.244'},{'HTTP': 'HTTP://114.104.135.251'},{'HTTP': 'HTTP://223.241.117.210'},{'HTTPS': 'HTTPS://125.126.117.30'},{'HTTPS': 'HTTPS://125.126.109.112'},{'HTTPS': 'HTTPS://125.126.113.184'},{'HTTP': 'HTTP://124.200.36.118'},{'HTTP': 'HTTP://115.219.105.158'},{'HTTP': 'HTTP://150.138.106.174'},{'HTTPS': 'HTTPS://115.219.107.158'},{'HTTP': 'HTTP://118.114.164.174'},{'HTTP': 'HTTP://202.107.233.123'},{'HTTPS': 'HTTPS://125.126.98.137'},{'HTTPS': 'HTTPS://125.126.107.48'},{'HTTP': 'HTTP://125.126.114.7'},{'HTTPS': 'HTTPS://125.126.114.247'},{'HTTPS': 'HTTPS://111.231.239.143'},{'HTTPS': 'HTTPS://115.223.64.38'},{'HTTPS': 'HTTPS://210.5.10.87'},{'HTTPS': 'HTTPS://58.254.220.116'},{'HTTP': 'HTTP://115.223.109.167'},{'HTTP': 'HTTP://115.223.96.231'},{'HTTPS': 'HTTPS://171.35.168.113'},{'HTTP': 'HTTP://114.239.211.175'},{'HTTP': 'HTTP://27.43.188.66'},{'HTTPS': 'HTTPS://117.88.4.162'},{'HTTP': 'HTTP://110.73.47.126'},{'HTTP': 'HTTP://171.35.173.121'},{'HTTP': 'HTTP://106.75.177.227'},{'HTTPS': 'HTTPS://218.75.69.50'},{'HTTP': 'HTTP://115.223.94.243'},{'HTTPS': 'HTTPS://124.93.201.59'},{'HTTP': 'HTTP://222.95.144.181'},{'HTTP': 'HTTP://222.95.241.80'},{'HTTP': 'HTTP://117.88.5.19'},{'HTTPS': 'HTTPS://223.241.116.201'},{'HTTP': 'HTTP://110.73.0.113'},{'HTTPS': 'HTTPS://117.88.4.242'},{'HTTP': 'HTTP://202.115.142.147'},{'HTTP': 'HTTP://117.88.5.253'},{'HTTPS': 'HTTPS://115.219.105.8'},{'HTTPS': 'HTTPS://171.35.170.144'},{'HTTPS': 'HTTPS://115.219.109.194'},{'HTTPS': 'HTTPS://120.39.216.129'},{'HTTPS': 'HTTPS://115.223.68.95'},{'HTTP': 'HTTP://115.219.104.57'},{'HTTP': 'HTTP://115.223.88.91'},{'HTTP': 'HTTP://121.237.149.165'},{'HTTPS': 'HTTPS://222.95.144.204'},{'HTTPS': 'HTTPS://121.33.220.158'},{'HTTPS': 'HTTPS://119.254.94.93'},{'HTTPS': 'HTTPS://175.148.79.80'},{'HTTPS': 'HTTPS://115.219.104.254'},{'HTTP': 'HTTP://121.40.162.239'},{'HTTP': 'HTTP://117.68.190.162'},{'HTTPS': 'HTTPS://163.204.244.185'},{'HTTP': 'HTTP://113.194.31.60'},{'HTTPS': 'HTTPS://182.92.220.212'},{'HTTPS': 'HTTPS://117.88.4.160'}

]
def login(using_proxy):
    url = 'http://glidedsky.com/login'

    h = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    }
    session = requests.Session()
    session.proxies=using_proxy
    session.headers = h
    token = session.get(url)
    _token = re.search(r'"_token" value="(.*?)"', token.text).group(1)
    print(_token)
    data = {
        "_token": _token,
        "email": "mickihuang@163.com",
        "password": "Fortchym21",
    }
    res = session.post(url, data=data)

    return  session
def write2html(filename,content):
    if os.path.exists("html"):
        pass
    else:
        os.mkdir(os.getcwd()+"/html")

    dir = os.getcwd()+"/html/"
    with open(dir+filename+'.html', "w", encoding="utf-8")as f:
        # write传入的是字符串
        f.write(content)
def test():

    # nums = 0
    global proxy
    for page in range(1,2):
        now_proxy = proxy.pop(3)
        session = login(now_proxy)

        html = session.get("http://www.glidedsky.com/level/web/crawler-ip-block-1?page={}".format(str(page)),proxies=now_proxy).text
        write2html("second",html)
    #     bs = BeautifulSoup(html,"lxml")
    #
    #     rows = bs.find_all("div",class_='col-md-1')
    #
    #     for row in rows:
    #         num= int (row.get_text())
    #         # print(num)
    #
    #         nums=nums+num
    #         # print(nums)
    # print(nums)
test()