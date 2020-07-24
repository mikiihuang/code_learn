__author__ = 'yumihuang'
# project name:codelearn
# time:2020-07-21
import random
import requests
from bs4 import BeautifulSoup
import time
from urllib import parse

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
    "Cookie":"JSESSIONID=1742F7C6EE8247803138F161E6068558; BIGipServerpool_vmportal_3333=!CjQ4qxgGqVs0uL7TYvoIeOVXnuYeK28CPGaxFDdnik2MabcBOQ1ua1MbTm8QNqKGvP6Y++qJ6DaG; BIGipServerpool_vmconsoleonest_8443=!eMvFNWni8+aS4vDTYvoIeOVXnuYeK790VKPBNAFD7VowkxU7cNSs+Y0/yPDoCNiweAYs1X1bingAeTE=; BIGipServerpool_vmportalsso_8443=!R4DbeCx68UtSIjXTYvoIeOVXnuYeK4XTYxOKIWTiQbUiBNHsoN1PJM893fgZWimtqwNhLchzQcDqxQ==; BIGipServerpool_vmapigateway=!m2TfgBhSOTN+QFLTYvoIeOVXnuYeK5DptzDFw9OA1iYNIY2fnsXdpja/ETdNeMQ/cj0N7kWmjMGv1Og=; BIGipServerpool_vmconsolenj_8443=!7neGRoszrZDV9zLTYvoIeOVXnuYeK+AKxg2xzBJVn+A7b99LwaLOqb5Xb0NZY6v2rmx0UsrreUsN37E=; BIGipServerpool_piwik_8001=!sasBkMFMFkMJ8gjTYvoIeOVXnuYeK6ciRz7UHHdx/GM0yL79P6Rq+7Su904sWgaioH/Gcc5p9u+vGw==; _gscu_233472779=95309920yykgtc60; _gscbrs_233472779=1; BIGipServerpool_op-msgqueue-static_5009=!QYYX0smRETBQhYvTYvoIeOVXnuYeK+ht30+5ZKAmIIEeDxhx1tgFgzolxK5YKoSr2i+vKkgaFf0jHzU=; BIGipServerpool_vipconsole_static_5009=!ebNfwYWjYzOoGIrTYvoIeOVXnuYeK866qJ1csVV4249klbxnS/sb5nTYbuuEN3+AoDaYxubkf1W8j4E=; BIGipServerpools_op_infocenter_static_5009=!iklcWa86xjCvlTrTYvoIeOVXnuYeK2GWLBAv4HuQ48XWpXhgWU/XzO23y0jnfqBOFfLRspp8f8cjf/E=; read=null; BIGipServerpool_vmconsolenj_3005=!OuM140HjeAKIVF7TYvoIeOVXnuYeK7L7IqsFhQC7d7UvH2Jqq1AtMATXFW0wU+rQ451EItnsD1bKrA==; SID=Set2; cfLatestRecordTimestamp=1595325056769; zg_did=%7B%22did%22%3A%20%2217370c976e5662-0d3f3ecc7a2fcf-396f7500-13c680-17370c976e6afc%22%7D; BIGipServerpool_vmportalssl_8443=!B4iRR9JSGh3fvqHTYvoIeOVXnuYeK1qg6E/9kj5ns4wiC9xS7a8667f1dQ3xUdr50RxGGJ3MJrr7ig==; ipLoc-djd=7a354512-cfd0-472c-a037-fd64ff160107; _pk_id.1.663d=a284326ba2c4e88a.1595309920.3.1595380425.1595380425.; WT_FPC=id=2f6a775c86742392fb51595311349982:lv=1595380425471:ss=1595380425471; zg_63df7be07da847be8e46cf4ae33c7c40=%7B%22sid%22%3A%201595383095995%2C%22updated%22%3A%201595383095995%2C%22info%22%3A%201595325118190%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22open.iot.10086.cn%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fopen.iot.10086.cn%2Fproductservice%2Fonenetdevboard%2F%22%7D; JSESSIONID=1DBB773D3119333C49A1AEAA0518CC17",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site":"same-origin",
    "Connection": "close"
    # "X-Requested-With": "XMLHttpRequest"

}
all_links = []

def get_first_url(url):

    base_url = "https://" + parse.urlparse(url).hostname
    print(base_url)
    resp = requests.get(url,headers=headers,verify=False).text
    # print(resp)
    soup = BeautifulSoup(resp,"lxml")
    print(soup.title)
    a_labels = soup.find_all('a', attrs={'href': True})
    url_now = []
    for a in a_labels:
        link = a.get("href")

        #未判空
        if link.startswith("javascript") or link.startswith("javascipt"):
            continue
        #相对路径
        elif link.startswith("/"):
            link = parse.urljoin(base_url,link)
            print(link)
        #去重
        if link in all_links:
            continue
        all_links.append(link)
        get_first_url(link)


            #失败后自动重试一次
            # flag = 1
            # cnt = 0
            # while flag == 1 and cnt < 2:
            #     try:
            #         cnt += 1
            #         log = link +"   " +str(verify_url(link))
            #         flag = -1
            #     except:
            #         time.sleep(3)

            # print(log)
            # write_log(log)

            # print(link)

# response = requests.get("https://ecloud.10086.cn/op-help-center/user/checkLogin",headers=headers,verify=False)
def get_next_url(url):
    pass
##请求url，返回状态码
def verify_url(url):
    requests.packages.urllib3.disable_warnings()
    resp = requests.get(url,headers=headers,verify=False)
    return resp.status_code

def write_log(strings):
    with open("log2.txt","a+") as f:
        f.write(strings+"\n")
# first_urls = get_first_url("https://ecloud.10086.cn/op-console-global/dashboard")
first_urls = get_first_url("https://ecloud.10086.cn")
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
# read_log('./log.txt')


