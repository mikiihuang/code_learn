# -*- coding: utf-8 -*-

#####使用Scrapy的简单爬虫demo:爬取腾讯招聘网站#########

import scrapy
from tencent.items import TencentItem
import json
page = 2
class TencentHireSpider(scrapy.Spider):
    name = 'tencent_hire'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?categoryId=40001001,40001002,40001003,40001004,40001005,40001006&pageIndex=1&pageSize=10']

    def parse(self, response):

        hire_list = json.loads(response.text)["Data"]["Posts"]
        # print(hire_list)

        for each in hire_list:
            hire_each = TencentItem()
            hire_each['hire_title'] = each['RecruitPostName']
            hire_each['hire_bu'] = each['BGName']
            hire_each['hire_place'] = each['LocationName']
            hire_each['hire_type'] = each['CategoryName']
            hire_each['hire_time'] = each['LastUpdateTime']
            # hire_each['hire_response'] = each['Responsibility']
            yield hire_each

        global page
        if page < 269:
            yield scrapy.Request(url='https://careers.tencent.com/tencentcareer/api/post/Query?categoryId=40001001,40001002,40001003,40001004,40001005,40001006&pageIndex={}&pageSize=10&language=zh-cn&area=cn'.format(page),callback=self.parse,dont_filter=True)
            page+= 1
