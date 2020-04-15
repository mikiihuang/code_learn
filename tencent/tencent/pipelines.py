# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv
class TencentCSVPipeline(object):
    def __init__(self):
        store_file  = os.path.dirname(__file__)+'/spiders/hireInfo.csv'
        self.file = open(store_file,"a+",encoding='utf-8',newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['title', 'bu', 'place', 'type', 'time'])
    def process_item(self, item, spider):
        self.writer.writerow([item['hire_title'],item['hire_bu'],item['hire_place'],item['hire_type'],item['hire_time']])
        return item
