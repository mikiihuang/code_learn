# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem
import json
page = 2
class TencentHireSpider(scrapy.Spider):
    name = 'tencent_hire'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?categoryId=40001001,40001002,40001003,40001004,40001005,40001006&pageIndex=1&pageSize=10']

    def parse(self, response):

 hire_each['hire_response'] = each['Responsibility']
            yield hire_each

        global page
        if page <5:
            yield scrapy.Request(url='https://careers.tencent.com/tencentcareer/api/post/Query?categoryId=40001001,40001002,40001003,40001004,40001005,40001006&pageIndex={}&pageSize=10&language=zh-cn&area=cn'.format(page),callback=self.parse,dont_filter=True)
            page+= 1
