# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#Here there are all the items that will be scrapped along the three spiders
class WsProjectItem(scrapy.Item):
    # define the fields for your item here like:
    link_country = scrapy.Field()
    link = scrapy.Field()
    text = scrapy.Field()
    pollution = scrapy.Field()
    date = scrapy.Field()
    pass
