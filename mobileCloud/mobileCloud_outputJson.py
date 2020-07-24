__author__ = 'yumihuang'
# project name:codelearn
# time:2020-07-22
#coding:utf-8



import re
import requests
from bs4 import BeautifulSoup
import time
import random
from urllib import parse
import json
import signal
import hashlib

user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
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
        "Cookie": "JSESSIONID=1742F7C6EE8247803138F161E6068558; BIGipServerpool_vmportal_3333=!CjQ4qxgGqVs0uL7TYvoIeOVXnuYeK28CPGaxFDdnik2MabcBOQ1ua1MbTm8QNqKGvP6Y++qJ6DaG; BIGipServerpool_vmconsoleonest_8443=!eMvFNWni8+aS4vDTYvoIeOVXnuYeK790VKPBNAFD7VowkxU7cNSs+Y0/yPDoCNiweAYs1X1bingAeTE=; BIGipServerpool_vmportalsso_8443=!R4DbeCx68UtSIjXTYvoIeOVXnuYeK4XTYxOKIWTiQbUiBNHsoN1PJM893fgZWimtqwNhLchzQcDqxQ==; BIGipServerpool_vmapigateway=!m2TfgBhSOTN+QFLTYvoIeOVXnuYeK5DptzDFw9OA1iYNIY2fnsXdpja/ETdNeMQ/cj0N7kWmjMGv1Og=; BIGipServerpool_vmconsolenj_8443=!7neGRoszrZDV9zLTYvoIeOVXnuYeK+AKxg2xzBJVn+A7b99LwaLOqb5Xb0NZY6v2rmx0UsrreUsN37E=; BIGipServerpool_piwik_8001=!sasBkMFMFkMJ8gjTYvoIeOVXnuYeK6ciRz7UHHdx/GM0yL79P6Rq+7Su904sWgaioH/Gcc5p9u+vGw==; _gscu_233472779=95309920yykgtc60; _gscbrs_233472779=1; BIGipServerpool_op-msgqueue-static_5009=!QYYX0smRETBQhYvTYvoIeOVXnuYeK+ht30+5ZKAmIIEeDxhx1tgFgzolxK5YKoSr2i+vKkgaFf0jHzU=; BIGipServerpool_vipconsole_static_5009=!ebNfwYWjYzOoGIrTYvoIeOVXnuYeK866qJ1csVV4249klbxnS/sb5nTYbuuEN3+AoDaYxubkf1W8j4E=; BIGipServerpools_op_infocenter_static_5009=!iklcWa86xjCvlTrTYvoIeOVXnuYeK2GWLBAv4HuQ48XWpXhgWU/XzO23y0jnfqBOFfLRspp8f8cjf/E=; read=null; BIGipServerpool_vmconsolenj_3005=!OuM140HjeAKIVF7TYvoIeOVXnuYeK7L7IqsFhQC7d7UvH2Jqq1AtMATXFW0wU+rQ451EItnsD1bKrA==; SID=Set2; cfLatestRecordTimestamp=1595325056769; zg_did=%7B%22did%22%3A%20%2217370c976e5662-0d3f3ecc7a2fcf-396f7500-13c680-17370c976e6afc%22%7D; BIGipServerpool_vmportalssl_8443=!B4iRR9JSGh3fvqHTYvoIeOVXnuYeK1qg6E/9kj5ns4wiC9xS7a8667f1dQ3xUdr50RxGGJ3MJrr7ig==; ipLoc-djd=7a354512-cfd0-472c-a037-fd64ff160107; _pk_id.1.663d=a284326ba2c4e88a.1595309920.3.1595380425.1595380425.; WT_FPC=id=2f6a775c86742392fb51595311349982:lv=1595380425471:ss=1595380425471; zg_63df7be07da847be8e46cf4ae33c7c40=%7B%22sid%22%3A%201595383095995%2C%22updated%22%3A%201595383095995%2C%22info%22%3A%201595325118190%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22open.iot.10086.cn%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fopen.iot.10086.cn%2Fproductservice%2Fonenetdevboard%2F%22%7D; JSESSIONID=1DBB773D3119333C49A1AEAA0518CC17",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Connection": "close"
        # "X-Requested-With": "XMLHttpRequest"

    }
def getHtml(url):
    #获取当前网址的域名
    base_url = "https://" + parse.urlparse(url).hostname
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url,headers=headers,verify=False)

        response.raise_for_status()
        html = response.text
        # md5_hash = hashlib.md5(html).hexdigest()

    except requests.RequestException as e:
        print(e)

    return base_url,html


def get_urls(html):
    """
    获取当前页面中所有的超链接的列表信息
    """
    links = []

    soup = BeautifulSoup(html, "lxml")
    a_lables = soup.find_all('a', attrs={'href': True})
    for link in a_lables:
        links.append(link.get('href'))
    return links


def save_json(murl, fileName):
    with open(fileName, 'a+',encoding="utf-8") as f:
        # f.writelines(murl+"\n")

        json.dump(murl,f,indent=2,ensure_ascii=False)

#验证url有效性，返回status_code和响应时间
def verify_url(url):
    requests.packages.urllib3.disable_warnings()
    try:
        resp = requests.get(url,headers=headers,verify=False)
        md5_hash = hashlib.md5(resp.text.encode("utf-8")).hexdigest()
        # print(hashlib.md5(resp.text.encode("utf-8")).hexdigest())
        return resp.status_code,resp.elapsed.total_seconds(),md5_hash
    except:
        pass

# class MyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, bytes):
#             return str(obj, encoding='utf-8');
#         return json.JSONEncoder.default(self, obj)


def Myhandler(signalnum, handler):
    global is_sigint_up
    is_sigint_up = True
    print("中断了")
    save_json(final_result, "interruptData.json")
    # exit()


def CrawlInfo(url):


    # crawl_queue = []  # 声明待爬队列:当前页面有哪些url
    hlinks = []

    base,html = getHtml(url)
    links = get_urls(html)
    global final_result
    final_result = []
    #检验a标签href的有效性


    signal.signal(signal.SIGINT, Myhandler)
    signal.signal(signal.SIGHUP, Myhandler)
    signal.signal(signal.SIGTERM, Myhandler)
    global is_sigint_up
    is_sigint_up = False
    while not is_sigint_up:

        for murl in links:

            murl_result={}
            if re.findall("^javasc(r)?ipt", murl) or len(murl)==0:
                continue
            elif re.findall("^/", murl):
                murl = parse.urljoin(base, murl)
            elif re.findall("^http", murl):
                murl = str(murl)

            #去重

            if murl not in crawl_queue and murl not in crawled_queue:
                murl_result['url'] = murl
                hlinks.append(murl)
                #处理verify_url方法走except异常分支返回为None的bug
                try:

                    murl_result["status_code"],murl_result["response_time"],murl_result["hash"] = verify_url(murl)
                    time.sleep(random.random() * 3)
                except:
                    murl_result["status_code"], murl_result["response_time"]="",""
                murl_result["condition"] = "Normal" if murl_result["status_code"] == 200 else "Abnormal!!!"

                print(murl_result)
                final_result.append(murl_result)
                # print(final_result)
                # murl_result=json.dumps(murl_result)
                # save_json(murl_result,"part.json")
                # log = murl +"   " +str(verify_url(murl))
                # print(log)
                # save_file(log,"3.txt")
            else:
                time.sleep(random.random() * 3)
                continue

            if is_sigint_up:
                break


    # print(final_result)
    for _ in hlinks:
        if _ not in crawl_queue and _ not in crawled_queue:
            crawl_queue.append(_)
            time.sleep(0.001)



if __name__ == "__main__":

    crawled_queue = []  # 已爬的
    global crawl_queue  #待爬的
    crawl_queue = []
    seedUrl = "https://ecloud.10086.cn/"

    CrawlInfo(seedUrl)

    crawled_queue.append(seedUrl)

    # result_list = []
    # 抓取队列中的信息为空，则退出循环
    try:
        while crawl_queue:
            url = crawl_queue.pop(0)
            global is_sigint_up
            if not is_sigint_up:
                CrawlInfo(url)
            else:
                break
            crawl_queue = list(set(crawl_queue))
            crawled_queue.append(url)
        save_json("dataAll.json")
    except:
        save_json("dataBreak.json")


