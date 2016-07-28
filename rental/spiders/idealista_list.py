import datetime
from urllib.parse import urlparse, urljoin
import socket
import scrapy

from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from scrapy.http import Request

from rental.items import RentalItem


class IdealistaListSpider(scrapy.Spider):
    name = 'idealista_list'
    allowed_domains = ['idealista.it']
    start_urls = ['https://www.idealista.it/affitto-case/milano-milano/']

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7'
    }

    def parse(self, response):
        # Get the next index URLs and yield Requests
        next_selector = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "icon-arrow-right-after", " " ))]//span//@href')
        for url in next_selector.extract():
            yield Request(urljoin(response.url, url))

        # Get item URLs and yield Requests
        item_selector = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "item-info-container", " " ))]')
        for lakas in item_selector:
            yield self.parse_item(lakas,response)

    def parse_item(self, selector,response):

        # Create the loader using the response
        l = ItemLoader(item=RentalItem(), selector=selector)
        l.add_xpath('price','(.//span[contains(@class, "item-price")]/text())[1]')
        l.add_xpath('size','.//small/text()[. = "m2"]/../../text()')
        l.add_xpath('rooms','.//small/text()[. = "locali"]/../../text()')
        l.add_xpath('address','.//a[contains(@class, "item-link")]/@title')
        l.add_xpath('elevator','.//span[text()="piano"]/../text()')
        #l.add_xpath('floor','(.//span[text()="piano"]/../../text())[1]')
        return l.load_item()
