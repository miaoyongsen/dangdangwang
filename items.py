# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #rank = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
    #pub_data = scrapy.Field()
