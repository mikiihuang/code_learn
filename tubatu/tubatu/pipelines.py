# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# {'content_id': '3082437',
#  'content_name': '热门面积102平简约三居客厅装修设计效果图片',
#  'content_url': 'http:////xiaoguotu.to8to.com/c3082437.html',
#  'nick_name': 0,
#  'pic_name': '',
#  'pic_url': 'https://pic1.to8to.com/case//social/day_20190521/145300d71d9f597bfc3c545fc02fc144.jpg'}

class TubatuPipeline(object):
    def process_item(self, item, spider):
        # print(item)
        # print(type(item))
        # print(len(item))
        with open('tu8tu.txt','a',encoding='utf-8') as f:
            f.write(str(item['content_id'])+'    '+item['content_name']+'    '+item['content_url']+'     '+str(item['nick_name'])+'   '+item['pic_name']+'     '+item['pic_url']+'\n')
        return item
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

# 自定义图片下载类，且继承于ImagesPipeline
class TubatuImagePipeline(ImagesPipeline):
    # def get_media_requests(self, item, info):
    #     # 根据image_urls中指定的url进行爬取，该方法默认即可
    #     pass

    def item_completed(self, results, item, info):
        # 图片下载完成之后，处理结果的方法，返回的是一个二元组
        # 返回的格式：(success, image_info_or_failure)  第一个元素表示图片是否下载成功；第二个元素是一个字典，包含了image的信息
        image_paths = [x["path"] for ok, x in results if ok]    # 通过列表生成式
        if not image_paths:
            raise DropItem("Item contains no images")   # 抛出异常，图片下载失败（注意要导入DropItem模块）
        return item

    def file_path(self, request, response=None, info=None):
        # 用于给下载的图片设置文件名称
        url = request.url
        file_name = url.split("/")[-1]  # 通过 / 来进行分割，选取最后一个
        # 如："https://pic.to8to.com/case/2018/08/27/20180827165930-fac62168_284.jpg"
        # 拆分后为：20180827165930-fac62168_284.jpg
        return file_name
