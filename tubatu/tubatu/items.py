# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TubatuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content_name = scrapy.Field()  # 装修名称
    content_id = scrapy.Field()  # 装修id
    content_url = scrapy.Field()  # 请求的url地址
    nick_name = scrapy.Field()  # 上传图片人的昵称
    # pic_url = scrapy.Field()  # 图片的url地址
    pic_name = scrapy.Field()  # 图片名称
    image_urls = scrapy.Field()
