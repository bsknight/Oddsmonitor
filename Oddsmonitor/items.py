# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OddsmonitorItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()	#company name
    init_win = scrapy.Field()
    init_draw = scrapy.Field()
    init_lose = scrapy.Field()
    now_win = scrapy.Field()
    now_draw = scrapy.Field()
    now_lose = scrapy.Field()
