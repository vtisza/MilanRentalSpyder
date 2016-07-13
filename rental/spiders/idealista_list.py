# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader

from rental.items import RentalItem


class IdealistaListSpider(CrawlSpider):
    name = 'idealista_list'
    allowed_domains = ['idealista.it']
    start_urls = ['https://www.idealista.it/affitto-case/milano/centro-storico/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[contains(concat( " ", @class, " " ), concat( " ", "item-link", " " ))]'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//*[contains(concat( " ", @class, " " ), concat( " ", "icon-arrow-right-after", " " ))]//span'), follow=True)
    )
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7'
    }

    def parse_item(self, response):
        l=ItemLoader(item=RentalItem(),response=response)
        l.add_xpath('price','//*[(@id = "main-info")]//*[contains(concat( " ", @class, " " ), concat( " ", "txt-big", " " )) and contains(concat( " ", @class, " " ), concat( " ", "txt-bold", " " ))]/text()')
        l.add_xpath('adress','//*[(@id = "addressPromo")]//*[contains(concat( " ", @class, " " ), concat( " ", "txt-bold", " " ))]/text()')
        l.add_value('url', response.url)
        return l.load_item()
