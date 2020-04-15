# -*- coding: utf-8 -*-
import scrapy
import json
import re
from tubatu.items import TubatuItem


class TubatuTestSpider(scrapy.Spider):
    name = 'tubatu_test'
    allowed_domains = ['https://xiaoguotu.to8to.com']
    start_urls = ['https://xiaoguotu.to8to.com/tuce//']

    def parse(self, response):
        all_pic_list = response.xpath("//div[@oldaid]")
        content_id_search = re.compile(r"(\d+)\.html")
        for item in all_pic_list:
            info = {}
            info['content_name'] = item.xpath("./div/a/text()").extract_first()
            # print(content_name)
            # print(type(content_name))
            info['content_url'] = "http://"+item.xpath("./div/a/@href").extract_first()
            # print(content_url)
            info['content_id'] = content_id_search.search(info['content_url']).group(1)
            content_ajax_url = "https://xiaoguotu.to8to.com/case/list?a2=0&a12=&a11={}&a6=&a3=&a10=2".format(info['content_id'])
            # print(content_ajax_url)
            yield scrapy.Request(url=content_ajax_url,callback=self.getDetail,dont_filter=True,meta=info)
        if response.xpath("//a[@id='nextpageid']"):
            now_page = int(response.xpath("//div[@class='pages']/strong/text()")).extract_first()
            next_page = "https://xiaoguotu.to8to.com/tuce/p_{}.html".format(now_page+1)
            yield scrapy.Request(url=next_page,callback=self.parse())

    def getDetail(self,response):
        # print(response.text)
        pic_dict_data = json.loads(response.text)['dataImg']
        # print(pic_dict_data)
        for pic_item in pic_dict_data:
            for item in pic_item['album']:
                tubatu_info = TubatuItem()
                tubatu_info['nick_name'] = item['l']['a']
                # tubatu_info['pic_url'] = "https://pic1.to8to.com/case/" + item['l']['s']
                tubatu_info['image_urls'] = ["https://pic1.to8to.com/case/" + item["l"]["s"]]
                tubatu_info['pic_name'] = item['l']['t']
                tubatu_info['content_name'] = response.request.meta['content_name']
                tubatu_info['content_id'] = response.request.meta['content_id']
                tubatu_info['content_url'] = response.request.meta['content_url']
                yield tubatu_info
