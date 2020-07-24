__author__ = 'yumihuang'
# project name:codelearn
# time:2020-07-21
import random
import requests
from bs4 import BeautifulSoup
import time

#随机切换userAgent
user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
                    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
                    ]

headers = {

    "User-Agent": random.choice(user_agent_list),
    "Cookie":"JSESSIONID=A185EBFEEDF5C6FC15903488A4BC7B8C; BIGipServerpool_vmportalssl_8443=!rUK8fnz+g7G46pXTYvoIeOVXnuYeKxsVkq7G4tjjTG1rUgG4I0rgtoFjxXa9H7e8IFSU30PeTvkIDZM=; BIGipServerpool_vmportal_3333=!CjQ4qxgGqVs0uL7TYvoIeOVXnuYeK28CPGaxFDdnik2MabcBOQ1ua1MbTm8QNqKGvP6Y++qJ6DaG; BIGipServerpool_vmconsoleonest_8443=!eMvFNWni8+aS4vDTYvoIeOVXnuYeK790VKPBNAFD7VowkxU7cNSs+Y0/yPDoCNiweAYs1X1bingAeTE=; BIGipServerpool_vmportalsso_8443=!R4DbeCx68UtSIjXTYvoIeOVXnuYeK4XTYxOKIWTiQbUiBNHsoN1PJM893fgZWimtqwNhLchzQcDqxQ==; BIGipServerpool_vmapigateway=!m2TfgBhSOTN+QFLTYvoIeOVXnuYeK5DptzDFw9OA1iYNIY2fnsXdpja/ETdNeMQ/cj0N7kWmjMGv1Og=; BIGipServerpool_vmconsolenj_8443=!7neGRoszrZDV9zLTYvoIeOVXnuYeK+AKxg2xzBJVn+A7b99LwaLOqb5Xb0NZY6v2rmx0UsrreUsN37E=; BIGipServerpool_piwik_8001=!sasBkMFMFkMJ8gjTYvoIeOVXnuYeK6ciRz7UHHdx/GM0yL79P6Rq+7Su904sWgaioH/Gcc5p9u+vGw==; _gscu_233472779=95309920yykgtc60; _gscbrs_233472779=1; _pk_ses.1.663d=*; BIGipServerpool_op-msgqueue-static_5009=!QYYX0smRETBQhYvTYvoIeOVXnuYeK+ht30+5ZKAmIIEeDxhx1tgFgzolxK5YKoSr2i+vKkgaFf0jHzU=; BIGipServerpool_vipconsole_static_5009=!ebNfwYWjYzOoGIrTYvoIeOVXnuYeK866qJ1csVV4249klbxnS/sb5nTYbuuEN3+AoDaYxubkf1W8j4E=; BIGipServerpools_op_infocenter_static_5009=!iklcWa86xjCvlTrTYvoIeOVXnuYeK2GWLBAv4HuQ48XWpXhgWU/XzO23y0jnfqBOFfLRspp8f8cjf/E=; read=null; WT_FPC=id=2f6a775c86742392fb51595311349982:lv=1595317859909:ss=1595317859909; BIGipServerpool_vmconsolenj_3005=!OuM140HjeAKIVF7TYvoIeOVXnuYeK7L7IqsFhQC7d7UvH2Jqq1AtMATXFW0wU+rQ451EItnsD1bKrA==; JSESSIONID=AD2285371055D88A5597CF3EF6D8923C; ipLoc-djd=7887a36c-85e9-4d74-a499-524e94ea448b; _pk_id.1.663d=a284326ba2c4e88a.1595309920.1.1595318992.1595309920.; _gscs_233472779=95309920egysme60|pv:58",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site":"same-origin",
    "Connection": "close"
    # "X-Requested-With": "XMLHttpRequest"

}
all_links = []
basic_url = "https://ecloud.10086.cn"
def get_first_url(url):

    resp = requests.get(url,headers=headers,verify=False).text
    # print(resp)
    soup = BeautifulSoup(resp,"lxml")
    print(soup.title)
    a_labels = soup.find_all('a', attrs={'href': True})

    for a in a_labels:
        link = a.get("href")
        if link.startswith("javascript") or link.startswith("javascipt"):
            continue
        elif not link.startswith("https"):
            link = basic_url+link
        #去重
        if link in all_links:
            continue

        #失败后自动重试一次
        flag = 1
        cnt = 0
        while flag == 1 and cnt < 2:
            try:
                cnt += 1
                log = link +"   " +str(verify_url(link))
                flag = -1
            except:
                time.sleep(3)

        print(log)
        write_log(log)
        all_links.append(link)
    return all_links
# response = requests.get("https://ecloud.10086.cn/op-help-center/user/checkLogin",headers=headers,verify=False)

##请求url，返回状态码
def verify_url(url):
    requests.packages.urllib3.disable_warnings()
    resp = requests.get(url,headers=headers,verify=False)
    return resp.status_code

def write_log(strings):
    with open("log.txt","a+") as f:
        f.write(strings+"\n")
# first_urls = get_first_url("https://ecloud.10086.cn/op-console-global/dashboard")
# first_urls = get_first_url("https://ecloud.10086.cn/home/")
def read_log(filename):
    with open(filename,'r') as f:
        contents = f.readlines()
        for line in contents:
            if len(line) !=0:
                first_url = line.strip().split("   ")[0]
                print(first_url)
                second_urls = get_first_url(first_url)
# for each in first_urls:
#     pass
read_log('./log.txt')

def get_noraml_url(url):
    resp = requests.get(url, headers=headers, verify=False).text
    # print(resp)
    soup = BeautifulSoup(resp, "lxml")
    print(soup.title)
    a_labels = soup.find_all('a', attrs={'href': True})

    for a in a_labels:
        link = a.get("href")
