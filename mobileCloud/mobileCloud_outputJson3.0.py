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
import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))
ALL_DATA = os.path.join(BASEDIR,"dataAll.json")
INTERRUPT_DATA = os.path.join(BASEDIR,"dataInterrupt.json")
SEEDURL = "https://ecloud.10086.cn/home/"


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
        "Cookie": "JSESSIONID=DB8E495FCDCB06204057774A4BC29B77; _gscu_233472779=95309920yykgtc60; zg_did=%7B%22did%22%3A%20%2217370c976e5662-0d3f3ecc7a2fcf-396f7500-13c680-17370c976e6afc%22%7D; zg_63df7be07da847be8e46cf4ae33c7c40=%7B%22sid%22%3A%201595414069856%2C%22updated%22%3A%201595414069856%2C%22info%22%3A%201595325118190%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22open.iot.10086.cn%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fopen.iot.10086.cn%2Fproductservice%2Fonenetdevboard%2F%22%7D; BIGipServerpool_vmportal_3333=!wnQwUMA1w2sNY4/TYvoIeOVXnuYeKwCiAccYOXghkuBuvJQhcMO2n0fd3SA9veV14HoHOJBVGQjH; BIGipServerpool_vmconsoleonest_8443=!dH7c4QslzJupqBfTYvoIeOVXnuYeKzBgZHter8MKF12EhwqIsI39OIIQCOKikZyslbhGibJAw1FMKWI=; BIGipServerpool_vmportalssl_8443=!/DOPsDY9eJBonALTYvoIeOVXnuYeKzVfuybNwPW8w8W4Nbp2+Sam9VFbCdVFclmrxSx8ZCcOdIWKsQ==; BIGipServerpool_vmportalsso_8443=!fJq5V8pXqf9YfCHTYvoIeOVXnuYeK3x94pw86b82FnhgkAk6kpAuBLMdvPN3i4Nbg6RCLcnp0Ei6Lw==; BIGipServerpool_vmapigateway=!JbH7DL/lFZ7h6GHTYvoIeOVXnuYeK2w7Prg5QazWj4r08Yxy/CBIC+Gb5Bc6Ba/nWm5Ix1mgoW4TQbs=; BIGipServerpool_vmconsolenj_8443=!PIbO+8dELszf9nzTYvoIeOVXnuYeKzCNj7uzTvKa/iinBT6/b9srpnDa60JdvbYmqYETPtf8IJUKvA==; _gscbrs_233472779=1; BIGipServerpool_piwik_8001=!7QRYJfMqLfkeiAjTYvoIeOVXnuYeK8CUSAmWI1VJ+XXmoKirag+5Q6B2m36/pe37xSYl5/8kU2mlIg==; WT_FPC=id=2f6a775c86742392fb51595311349982:lv=1595840802147:ss=1595840802147; OBS_SID=Set2; BIGipServerpools_op_infocenter_static_5009=!GULdofNJD8TWIHDTYvoIeOVXnuYeK7hyPLAFYuIKNjriWSEqV+2rLVuOzDfaYcwQnHH/9NuR/zP0yDU=; BIGipServerpool_vipconsole_static_5009=!/CPhneJFHB8nC2zTYvoIeOVXnuYeK4T1lB4KWLizhrsu6ge1EuvnUN+Kq0JOu+gWAb3YHj7I5pVA1QE=; ipLoc-djd=7816445f-cc4c-484f-be78-6fbbd2a8f59b; _gscs_233472779=95839215t0mzaq14|pv:34; _pk_id.1.663d=a284326ba2c4e88a.1595309920.9.1595843036.1595843036.; _pk_ses.1.663d=*; JSESSIONID=DCEFB8657C99E0EA132B30B7BBE953E0",
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
    final = []
    soup = BeautifulSoup(html, "lxml")
    a_lables = soup.find_all('a', attrs={'href': True})
    for link in a_lables:
        links.append(link.get('href'))
    for one in links:
        if one not in final:
            final.append(one)
    return final


def save_json(murl, fileName):
    with open(fileName, 'a+',encoding="utf-8") as f:
        # f.writelines(murl+"\n")

        json.dump(murl,f,indent=2,ensure_ascii=False)

# 取响应为非200的url
def write_url(filename,url,status):
    with open(filename,"a") as f:
        f.write(url+"       "+str(status)+"\n")

#验证url有效性，返回status_code和响应时间
def verify_url(url):
    requests.packages.urllib3.disable_warnings()
    try:
        resp = requests.get(url,headers=headers,verify=False)
        md5_hash = hashlib.md5(resp.text.encode("utf-8")).hexdigest()
        time_now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        # print(hashlib.md5(resp.text.encode("utf-8")).hexdigest())
        return resp.status_code,resp.elapsed.total_seconds(),md5_hash,time_now
    except:
        pass


def Myhandler(signalnum, handler):
    global is_sigint_up
    is_sigint_up = True
    print("中断了!!")
    save_json(final_result, INTERRUPT_DATA)
    # exit()


def CrawlInfo(url):

    # crawl_queue = []  # 声明待爬队列:当前页面有哪些url
    hlinks = []
    base,html = getHtml(url)
    links = get_urls(html)
    print(links)

    global final_result

    #检验a标签href的有效性


    signal.signal(signal.SIGINT, Myhandler)
    signal.signal(signal.SIGHUP, Myhandler)
    signal.signal(signal.SIGTERM, Myhandler)
    global is_sigint_up
    is_sigint_up = False

    # 处理未中断时陷入死循环的bug
    # while not is_sigint_up:

    for murl in links:
        if not is_sigint_up:
            murl_result={}
            if re.findall("^javasc(r)?ipt", murl) or len(murl)==0:
                continue
            elif re.findall("^http", murl):
                murl = str(murl)
            else:
                murl = parse.urljoin(base, murl)


            #去重
            if murl not in crawl_queue and murl not in crawled_queue and murl!=url:
                murl_result['url'] = murl
                hlinks.append(murl)
                #处理verify_url方法走except异常分支返回为None的bug
                try:
                    murl_result["status_code"],murl_result["response_time"],murl_result["hash"],murl_result["time"] = verify_url(murl)
                    time.sleep(random.random() * 3)
                except:
                    murl_result["status_code"], murl_result["response_time"]="",""
                murl_result["condition"] = "Normal" if murl_result["status_code"] == 200 else "Abnormal!!!"
                if murl_result["status_code"] != 200:
                    write_url("errorURL.txt",murl_result["url"],murl_result["status_code"])
                else:
                    pass
                print(murl_result)
                final_result.append(murl_result)

            else:
                time.sleep(random.random() * 3)
                continue

        if is_sigint_up:
            break


    # print(final_result)
    for _ in hlinks:
        if _ not in crawl_queue and _ not in crawled_queue and murl!=url:
            crawl_queue.append(_)
            time.sleep(0.001)
        else:
            pass



if __name__ == "__main__":

    crawled_queue = []  # 已爬的
    global crawl_queue  #待爬的
    crawl_queue = []
    final_result = []
    seedUrl = SEEDURL

    CrawlInfo(seedUrl)

    crawled_queue.append(seedUrl)


    while crawl_queue:
        url = crawl_queue.pop(0)
        print(url)
        global is_sigint_up
        if not is_sigint_up:
            CrawlInfo(url)
        else:
            break
        crawl_queue = list(set(crawl_queue))
        crawled_queue.append(url)
    save_json(final_result,ALL_DATA)



