# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RentalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    adress=scrapy.Field()
    price=scrapy.Field()
    url=scrapy.Field()

class IngatlanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    adress1=scrapy.Field()
    adress2=scrapy.Field()
    adress3=scrapy.Field()
    price=scrapy.Field()
    size=scrapy.Field()
    rooms=scrapy.Field()
    lon=scrapy.Field()
    lan=scrapy.Field()
    date=scrapy.Field()
    rentid=scrapy.Field()
