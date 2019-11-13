# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#  https://www.fpzw.com/top/allvote_1.html

class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    list_url = scrapy.Field()
    list_name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    num = scrapy.Field()
    file_name = scrapy.Field()
    desc = scrapy.Field()
    pass

class ArrBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # name = scrapy.Field()
    # link = scrapy.Field()
    # time = scrapy.Field()
    # types = scrapy.Field()
    # auther = scrapy.Field()
    pass

