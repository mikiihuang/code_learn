__author__ = 'yumihuang'
# project name:codelearn
# time:2020-07-22
import requests
import random

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
# resp = requests.get("https://ecloud.10086.cn/solution/smartCity/",headers=headers,verify=False)
# print(resp.status_code)

# from urllib import parse
# url = "https://ecloud.10086.cn/product/buy/vm"
# host = "https://"+ parse.urlparse(url).hostname
# print(parse.urljoin(host,"/usercenter/dashboard"))
# import re
# def helper(ss):
#     if re.match(r'javasc(r)?ipt',ss):
#         print("OK")
#     else:
#         print("No")
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
        return f.read().encode("utf-8")

resp = requests.get("https://ecloud.10086.cn/home/solution/common/safety",headers=headers,verify=False)
print(resp)
# print(resp.text)
# resp2 = requests.get("https://ecloud.10086.cn/home/solution/common/safety",headers=headers,verify=False)
# print("__________________________")
# print(resp2.text)
# # assert resp.text ==resp2.text
# a = read_file("1.txt")
# assert a == resp.text
# print(a)
#
# # a="asdfg".encode("utf-8")
# print(hashlib.md5(a).hexdigest())