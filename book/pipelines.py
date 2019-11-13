# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# encoding=utf8
import sys

import codecs
import json
import os
import re
from book.items import BookItem

reload(sys)
sys.setdefaultencoding('utf8')

class BooksPipeline(object):
    def __init__(self):
        self.content_list = []
        self.content_list_name = {}
    def open_spider(self, spider):
        pass
    def process_item(self, item, spider):
        self.content_list.append(item)
        return item
    def close_spider(self,spider):
        list_sorted = sorted(self.content_list, key=lambda x: x['num'])
        for item in list_sorted:
            self.file = open(item['file_name'], 'a')
            if item["num"]==1 :
                self.file.write("%s\n" % (item['desc']))
            self.file.write("(%s).%s \n" % (item['num'], item['title']))
            self.file.write("\n\n"+''.join(item['content']).replace(" ", '').replace("\r\n", "").replace("\n\n", "") + "\n\n")
            self.file.close()