# -*- coding: utf-8 -*-
import scrapy
from  politicNews.items import PoliticnewsItem

class NewsSpiderSpider(scrapy.Spider):
    name = 'news_spider'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    def parse(self, response):

        for item in response.xpath('//li[@class="clear"]'):
            each = {}
            each['id']=item.xpath('./span[@class="state1"]/text()').extract_first()
            each['url'] = "http://wz.sun0769.com/"+item.xpath('./span[@class="state3"]/a/@href').extract_first()
            each['title'] = item.xpath('./span[@class="state3"]/a/text()').extract_first()
            yield scrapy.Request(url=each['url'],callback=self.parse_item,meta=each)
        #只爬5页意思意思吧
        for page_id in range(2,5):
            page_url = "http://wz.sun0769.com/political/index/politicsNewest?id=1&page="+str(page_id)
            yield scrapy.Request(url=page_url,callback=self.parse)
    def parse_item(self,response):
        print(response.request.meta['url'])
        content_box = response.xpath('//div[@class="details-box"]')
        news_info = PoliticnewsItem()
        news_info['title'] = response.request.meta['title']
        news_info['content'] = content_box.xpath('//pre/text()').extract()
        # print(news_info)

        news_info['id'] = response.request.meta['id']
        news_info['url'] = response.request.meta['url']
        # print(news_info['title'])
        # print(news_info['title'])
        yield news_info
