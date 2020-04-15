# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hire_title = scrapy.Field()
    hire_bu = scrapy.Field()
    hire_place = scrapy.Field()
    hire_type = scrapy.Field()
    hire_time = scrapy.Field()
    # hire_response = scrapy.Field()
