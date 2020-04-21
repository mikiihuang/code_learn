# -*- coding: utf-8 -*-
import scrapy
import requests
import json
from scrapy.http import Request,FormRequest
# 请求登陆接口
headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
            "Cookie": "anonymid=k2d1dhua3wnq8n; _r01_=1; jebe_key=6332cccf-cf92-42da-b1e1-8008c0f81529%7C942d56a8bbc6be98b87d52116baa0cca%7C1572425254773%7C1%7C1572425258418; taihe_bi_sdk_uid=44f5abf2962d5916d5b7e56495613767; __utma=151146938.1882791334.1581756718.1581756718.1582369501.2; __utmz=151146938.1582369501.2.2.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/567835129/profile; ln_uact=18810400465; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20200215/1655/main_1AWt_ae700000f2b11986.jpg; depovince=GW; JSESSIONID=abc9neOKNelFy5U08Mcgx; ick_login=6c3ec253-82ec-4c6d-b7ca-5fa52251d830; taihe_bi_sdk_session=7fb5118ae784ef4730206a16d34c2e19; first_login_flag=1; loginfrom=null; jebe_key=6332cccf-cf92-42da-b1e1-8008c0f81529%7C942d56a8bbc6be98b87d52116baa0cca%7C1587083361465%7C1%7C1587083361826; jebecookies=9b859bc0-eaaa-4f85-ae75-e5434c591d72|||||; _de=F670F88B177C1A259063A68F0503E92A",
            "Host": "www.renren.com",
            "Origin": "http://www.renren.com",
            # "Referer": "http://www.renren.com/SysHome.do",
            "X-Requested-With": "XMLHttpRequest",

        }
 # 请求验证码接口
headers2 = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",

            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
            "Cookie": "anonymid=k2d1dhua3wnq8n; _r01_=1;  __utma=151146938.1882791334.1581756718.1581756718.1582369501.2; __utmz=151146938.1582369501.2.2.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/567835129/profile; ln_uact=18810400465; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20200215/1655/main_1AWt_ae700000f2b11986.jpg; depovince=GW; ick_login=6c3ec253-82ec-4c6d-b7ca-5fa52251d830; taihe_bi_sdk_session=7fb5118ae784ef4730206a16d34c2e19; first_login_flag=1; loginfrom=null; jebe_key=6332cccf-cf92-42da-b1e1-8008c0f81529%7C942d56a8bbc6be98b87d52116baa0cca%7C1587083361465%7C1%7C1587083361826; jebecookies=9b859bc0-eaaa-4f85-ae75-e5434c591d72|||||; _de=F670F88B177C1A259063A68F0503E92A",
            "Host": "icode.renren.com",
            "Upgrade-Insecure-Requests": "1",

        }

class RenrenSpiderSpider(scrapy.Spider):
    name = 'renren_spider'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/567835129/profile']



    def start_requests(self):
        return [scrapy.Request(url='http://www.renren.com/567835129/profile', callback=self.login,
                               meta={"cookiejar": 1})]

    def login(self, response):
        r_keyheader={
            "Accept": "*/*",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
            "Cookie": "anonymid=k2d1dhua3wnq8n; _r01_=1; taihe_bi_sdk_uid=44f5abf2962d5916d5b7e56495613767; __utma=151146938.1882791334.1581756718.1581756718.1582369501.2; __utmz=151146938.1582369501.2.2.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/567835129/profile; ln_uact=18810400465; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20200215/1655/main_1AWt_ae700000f2b11986.jpg; depovince=GW; ick_login=6c3ec253-82ec-4c6d-b7ca-5fa52251d830; taihe_bi_sdk_session=7fb5118ae784ef4730206a16d34c2e19; first_login_flag=1; loginfrom=null; jebe_key=6332cccf-cf92-42da-b1e1-8008c0f81529%7C942d56a8bbc6be98b87d52116baa0cca%7C1587083361465%7C1%7C1587083361826; _de=F670F88B177C1A259063A68F0503E92A; jebecookies=6a2c1560-9adc-430d-bff1-c7d47db0991d|||||",
            "Host": "login.renren.com",
            "Origin": "http://www.renren.com",
            "Referer": "http://login.renren.com/ajaxproxy.htm",
            "X-Requested-With": "XMLHttpRequest",

        }
        get_rkey = requests.get("http://login.renren.com/ajax/getEncryptKey",headers=r_keyheader).text
        r_key_value = json.loads(get_rkey)['rkey']
        print(r_key_value)
        data = {
            "email": "18810400465",

            'origURL': 'http://www.renren.com/home',
            'domain': 'renren.com',
            'key_id': '1',
            'captcha_type': 'web_login',
            # 这个加密之后的密码直接复制
            'password': '96a837fc9a233c64b19eac4fd9243be5d00afe86c7b7644ff87515d60e5b5729',
            'rkey': r_key_value,
            'f': 'http%3A%2F%2Fwww.renren.com%2F567835129',
        }
        captcha = response.xpath('//label[@class="codetip"]').extract()
        if len(captcha)==0:
            data_load = data
        else:
            print("有验证码")
            url = "http://icode.renren.com/getcode.do?t=web_login&rnd=Math.random()"
            icode =requests.get(url,headers=headers2)
            if icode.status_code == 200:
                with open('captcha.jpg','wb') as f:
                    f.write(icode.content)
            print("此次登录有验证码，请查看本地captcha图片输入验证码:")

            captcha_value = input()
            data_load = data.update({'icode':captcha_value})

        return [FormRequest(url="http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=202035910728",headers=headers,method='POST', meta={"cookiejar": response.meta["cookiejar"]}, formdata=data_load,callback=self.after_login, dont_filter=True)]

    def after_login(self, resonse):

        print(resonse.body.decode("utf-8"))
        if "黄亚美" in resonse.body.decode("utf-8"):
            print("登陆成功")
        else:
            print("失败！！！")
        # title = resonse.xpath('//div/h2[@class="ContentItem-title"]/text()').extract_first()
        # print(title)


    def parse(self, response):
        pass
