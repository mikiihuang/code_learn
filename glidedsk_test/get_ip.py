__author__ = 'yumihuang'
# project name:codelearn
# time:2020-04-20
import requests
from lxml import etree
import time
import random
import csv
from bs4 import BeautifulSoup

def test_ip(ip_address):
    '''
    测试ip是否可用
    :param ip_address: 代理ip
    '''
    # url = 'http://icanhazip.com/'
    url = 'https://www.baidu.com'
    headers = {
        # headers 头部文件
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
    }
    ip_pool = []
    for ip_test in ip_address:
        print(ip_test)
        try:
            # print(ip_test)
            response = requests.get(url=url, headers=headers, proxies=ip_test, timeout=5)
            print(response.status_code)
            # print(response)
            if response.status_code == 200:
                # print(ip_test)
                ip_pool.append(ip_test)
                print(ip_pool)
            time.sleep(random.randint(2, 8))
        except Exception as e:
            pass

    files_save(ip_pool)


def files_save(ip_list):
    '''
    将可用代理ip保存
    :param ip_list:代理ip
    :return:
    '''
    with open('./代理ip.csv', 'a+', encoding='utf-8')as f:
        write = csv.writer(f)
        write.writerow(ip_list)
    pass


def get_page_data(nums):
    '''
    获取西刺代理的页面信息
    :return:
    '''
    ip_list = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
    }
    for i in range(nums, nums + 1):
        url = "https://www.xicidaili.com/nn/{}".format(i)
        response = requests.request('get', url=url, headers=headers).text
        page_data = BeautifulSoup(response,"lxml")

        page_infos = page_data.find_all("tr")

        ip_list=[]
        for info in page_infos[1:]:
            # print(info)
            ip_dict={}
            ip_add = BeautifulSoup(str(info),"lxml").find_all("td")[1]
            ip_type = BeautifulSoup(str(info),"lxml").find_all("td")[5]
            ip_dict[ip_type.text] = ip_type.text + "://" +str(ip_add.text)

            ip_list.append(ip_dict)
    test_ip(ip_list)



if __name__ == '__main__':
    '''
    爬取代理ip时应注意
    需要测试此ip是否可用
    爬取速度
    分析：
    url信息
    页面      url
          https://www.xicidaili.com/nn/
          https://www.xicidaili.com/nn/2
          https://www.xicidaili.com/nn/3

    '''
    # nums = int(input("请输入爬取页数>>"))
    nums = 2
    get_page_data(nums)