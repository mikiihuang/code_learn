__author__ = 'yumihuang'
# project name:codelearn
# time:2020-07-22
import requests
import random

user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
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
    "Cookie":"JSESSIONID=3D819D39B7C495E8592BABBE8CC0928A; _gscu_233472779=95309920yykgtc60; zg_did=%7B%22did%22%3A%20%2217370c976e5662-0d3f3ecc7a2fcf-396f7500-13c680-17370c976e6afc%22%7D; zg_63df7be07da847be8e46cf4ae33c7c40=%7B%22sid%22%3A%201595414069856%2C%22updated%22%3A%201595414069856%2C%22info%22%3A%201595325118190%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22open.iot.10086.cn%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fopen.iot.10086.cn%2Fproductservice%2Fonenetdevboard%2F%22%7D; BIGipServerpool_vmportal_3333=!wnQwUMA1w2sNY4/TYvoIeOVXnuYeKwCiAccYOXghkuBuvJQhcMO2n0fd3SA9veV14HoHOJBVGQjH; BIGipServerpool_vmconsoleonest_8443=!dH7c4QslzJupqBfTYvoIeOVXnuYeKzBgZHter8MKF12EhwqIsI39OIIQCOKikZyslbhGibJAw1FMKWI=; BIGipServerpool_vmportalssl_8443=!/DOPsDY9eJBonALTYvoIeOVXnuYeKzVfuybNwPW8w8W4Nbp2+Sam9VFbCdVFclmrxSx8ZCcOdIWKsQ==; BIGipServerpool_vmportalsso_8443=!fJq5V8pXqf9YfCHTYvoIeOVXnuYeK3x94pw86b82FnhgkAk6kpAuBLMdvPN3i4Nbg6RCLcnp0Ei6Lw==; BIGipServerpool_vmapigateway=!JbH7DL/lFZ7h6GHTYvoIeOVXnuYeK2w7Prg5QazWj4r08Yxy/CBIC+Gb5Bc6Ba/nWm5Ix1mgoW4TQbs=; BIGipServerpool_vmconsolenj_8443=!PIbO+8dELszf9nzTYvoIeOVXnuYeKzCNj7uzTvKa/iinBT6/b9srpnDa60JdvbYmqYETPtf8IJUKvA==; _gscbrs_233472779=1; ipLoc-djd=47259c2b-20b2-464c-be16-1aeecb6c93d8; _pk_id.1.663d=a284326ba2c4e88a.1595309920.8.1595840801.1595840801.; BIGipServerpool_piwik_8001=!7QRYJfMqLfkeiAjTYvoIeOVXnuYeK8CUSAmWI1VJ+XXmoKirag+5Q6B2m36/pe37xSYl5/8kU2mlIg==; WT_FPC=id=2f6a775c86742392fb51595311349982:lv=1595840802147:ss=1595840802147; OBS_SID=Set2; BIGipServerpools_op_infocenter_static_5009=!GULdofNJD8TWIHDTYvoIeOVXnuYeK7hyPLAFYuIKNjriWSEqV+2rLVuOzDfaYcwQnHH/9NuR/zP0yDU=; BIGipServerpool_vipconsole_static_5009=!/CPhneJFHB8nC2zTYvoIeOVXnuYeK4T1lB4KWLizhrsu6ge1EuvnUN+Kq0JOu+gWAb3YHj7I5pVA1QE=; _gscs_233472779=95839215t0mzaq14|pv:25; JSESSIONID=E459486067DDAE544016696EF1185818",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site":"same-origin",
    "Connection": "close"
    # "X-Requested-With": "XMLHttpRequest"

}
# resp = requests.get("https://ecloud.10086.cn/solution/smartCity/",headers=headers,verify=False)
# print(resp.status_code)

# from urllib import parse
# url = "https://ecloud.10086.cn/product/buy/vm"
# host = "https://"+ parse.urlparse(url).hostname
# print(parse.urljoin(host,"/usercenter/dashboard"))
import re
def helper(ss):
    if re.match(r'^/',ss):
        print("OK")
    else:
        print("No")
# helper("javascript")
# helper("javascipt")
# helper("javascript:(0)")
# helper("javascipt:(0)")
# helper("javaScript:(0)")
# def test(num):
#     global a
#     a = []
#     for i in range(num):
#         if i%2 ==0:
#             a.append(i)
#     print(a)
# test(4)
ll = [{'url': 'https://ecloud.10086.cn/home/', 'status_code': 200, 'response_time': 0.428596, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/op-help-center', 'status_code': 200, 'response_time': 0.145533, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/op-console-global/subsystem?type=infocenter', 'status_code': 200, 'response_time': 0.206012, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/op-console-global/dashboard', 'status_code': 200, 'response_time': 0.218575, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/user/goRegister', 'status_code': 200, 'response_time': 0.157791, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/market/all', 'status_code': 200, 'response_time': 0.164439, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/vm', 'status_code': 200, 'response_time': 0.402424, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/gpu', 'status_code': 200, 'response_time': 0.376266, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/autoscaling', 'status_code': 200, 'response_time': 0.383138, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/ironic', 'status_code': 200, 'response_time': 0.355288, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/containerser', 'status_code': 200, 'response_time': 0.586511, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/caasimage', 'status_code': 200, 'response_time': 0.375128, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/vmbak', 'status_code': 200, 'response_time': 0.299773, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/mirrorservice', 'status_code': 200, 'response_time': 0.33283, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/dedicatedcloud', 'status_code': 200, 'response_time': 0.36729, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/database', 'status_code': 200, 'response_time': 0.371103, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/redis', 'status_code': 200, 'response_time': 0.379698, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/postgresql', 'status_code': 200, 'response_time': 0.318114, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/districache', 'status_code': 200, 'response_time': 0.329125, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/clouddb', 'status_code': 200, 'response_time': 0.296781, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/dds', 'status_code': 200, 'response_time': 0.348079, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/dbmt', 'status_code': 200, 'response_time': 0.3722, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/rocketmq', 'status_code': 200, 'response_time': 0.369911, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/kafka', 'status_code': 200, 'response_time': 0.367577, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/mqtt', 'status_code': 200, 'response_time': 0.376227, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/inform', 'status_code': 200, 'response_time': 0.376072, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/onest', 'status_code': 200, 'response_time': 0.373848, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/bs', 'status_code': 200, 'response_time': 0.374146, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/space', 'status_code': 200, 'response_time': 0.363402, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/gateway', 'status_code': 200, 'response_time': 0.372431, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/nas', 'status_code': 200, 'response_time': 0.301436, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/bsbak', 'status_code': 200, 'response_time': 0.336997, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/fcache', 'status_code': 200, 'response_time': 0.373447, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/cbackup', 'status_code': 200, 'response_time': 0.372144, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/monitor', 'status_code': 200, 'response_time': 0.376417, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/api', 'status_code': 200, 'response_time': 0.357247, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/audit', 'status_code': 200, 'response_time': 0.387165, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/journal', 'status_code': 200, 'response_time': 0.370757, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/apm', 'status_code': 200, 'response_time': 0.278795, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/uidauth', 'status_code': 200, 'response_time': 0.363725, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/drs', 'status_code': 200, 'response_time': 0.473309, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/hostmigration', 'status_code': 200, 'response_time': 0.574625, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/icp/recordIntroduction', 'status_code': 200, 'response_time': 0.199539, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/apig', 'status_code': 200, 'response_time': 0.392423, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/vpc', 'status_code': 200, 'response_time': 0.348961, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/eip', 'status_code': 200, 'response_time': 0.30031, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/ipv6convert', 'status_code': 200, 'response_time': 0.3661, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/vlb', 'status_code': 200, 'response_time': 0.379696, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/nat', 'status_code': 200, 'response_time': 0.3778, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/cbwp', 'status_code': 200, 'response_time': 0.361347, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/sharedfp', 'status_code': 200, 'response_time': 0.378117, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/sslvpn', 'status_code': 200, 'response_time': 0.364771, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/ipsecvpn', 'status_code': 200, 'response_time': 0.386415, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/conjoining', 'status_code': 200, 'response_time': 0.371501, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/cdn', 'status_code': 200, 'response_time': 0.37632, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/icdn', 'status_code': 200, 'response_time': 0.385491, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/cloudnet', 'status_code': 200, 'response_time': 0.352604, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/wire', 'status_code': 200, 'response_time': 0.331437, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/broadband', 'status_code': 200, 'response_time': 0.286467, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/dns', 'status_code': 200, 'response_time': 0.411657, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/vpcnode', 'status_code': 200, 'response_time': 0.404012, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/transcode', 'status_code': 200, 'response_time': 0.381907, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/vod', 'status_code': 200, 'response_time': 0.361672, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/live', 'status_code': 200, 'response_time': 0.372851, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/obs', 'status_code': 200, 'response_time': 0.373048, 'condition': 'Normal'}, {'url': 'https://ecloud.10086.cn/home/product-introduction/eds', 'status_code': 200, 'response_time': 0.472132, 'condition': 'Normal'}]
# import json
# print(json.dumps(ll))
def dps(Root_Node):
    if Root_Node is None:
        return
    if Root_Node.lChild:
        return dps(Root_Node.lChild)

    if Root_Node.rChild:
        return dps(Root_Node.rChild)

def bfs(Root_Node):
    if Root_Node is None:
        return
    queue = []
    Node = Root_Node
    queue.append(Node)
    while queue:
        Node = queue.pop(0)
        if Node.lChild:
            queue.append(Node.lChild)
        if Node.rChild:
            queue.append(Node.rChild)
import hashlib

def read_file(filename):
    with open(filename) as f:
        return f.readlines()
def write_file(filename,strings):
    with open(filename,"w") as f:
        f.write(strings)

# resp1 = requests.get("https://cloud-a.cmecloud.cn/product/product-intro.html?name=dns",headers=headers,verify=False)
# print(resp1.text)
#
# resp2 = requests.get("https://ecloud.10086.cn/home/solution/common/safety",headers=headers,verify=False)
# write_file("resp2.txt",resp2.text)

# print(resp.text)
# resp2 = requests.get("https://ecloud.10086.cn/home/solution/common/safety",headers=headers,verify=False)
# print("__________________________")
# print(resp2.text)
# # assert resp.text ==resp2.text
# a = read_file("1.txt")
# b = read_file("2.txt")
# assert len(a) == len(b)
# for line in range(len(a)):
#     if set(a[line])-set(b[line]) !=set():
#         print(line)
#
#
# ll=["https:ww.njdaa.com"]
# print(type(ll.pop(0)))
    # print(set(a[line])-set(b[line]))
    # print(a[line]-b[line])
# assert a == resp.text
# print(a)
#
# # a="asdfg".encode("utf-8")
# print(hashlib.md5(a).hexdigest())

import os
# print(os.getcwd())
base = os.path.dirname(os.path.abspath(__file__))
dir = os.path.join(base,"all.json")
print(dir)
# BASEDIR = os.getcwd()
