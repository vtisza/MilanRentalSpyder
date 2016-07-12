# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from rental.items import RentalItem


class IdealistaSpider(scrapy.Spider):
    name = "idealista"
    allowed_domains = ["web"]
    start_urls = (
        'https://www.idealista.it/immobile/10003307/?xtor=EPR-453-%5Bexpress_alerts_20160708%5D-20160708-%5Binmueble_foto%5D-%5B%5D-20160708164508&ident=Z8vdMekiGXQWloSmQ7Tqx9JiKkGtqWP%2BLC%2FCuqFeuz0t%2FiwFZqgDdwyP6BiQvmWE&adId=10003307&xts=402916',
    )
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7'
    }

    def parse(self, response):
        l=ItemLoader(item=RentalItem(),response=response)
        l.add_xpath('price','//*[(@id = "main-info")]//*[contains(concat( " ", @class, " " ), concat( " ", "txt-big", " " )) and contains(concat( " ", @class, " " ), concat( " ", "txt-bold", " " ))]/text()')
        l.add_xpath('adress','//*[(@id = "addressPromo")]//*[contains(concat( " ", @class, " " ), concat( " ", "txt-bold", " " ))]/text()')
        l.add_value('url', response.url)

        return l.load_item()
