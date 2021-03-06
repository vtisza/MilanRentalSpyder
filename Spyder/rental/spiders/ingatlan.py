import datetime
from urllib.parse import urlparse, urljoin
import socket
import scrapy

from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from scrapy.http import Request

from rental.items import IngatlanItem
from scrapy.selector import Selector


class IngatlanSpider(scrapy.Spider):
    name = "ingatlan"
    allowed_domains = ["ingatlan.com"]

    # Start on the first index page
    start_urls = (
        'http://ingatlan.com/lista/elado+lakas+budapest',
    )

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7'
    }

    def parse(self, response):
        # Get the next index URLs and yield Requests
        next_selector = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "next", " " ))]//@href')
        for url in next_selector.extract():
            yield Request(urljoin(response.url, url))

        # Get item URLs and yield Requests
        item_selector = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "list-row", " " ))]')
        for lakas in item_selector:
            yield self.parse_item(lakas,response)

    def parse_item(self, selector,response):

        # Create the loader using the response
        l = ItemLoader(item=IngatlanItem(), selector=selector)

        # Load fields using XPath expressions
        l.add_xpath('price', './/*[contains(concat( " ", @class, " " ), concat( " ", "price-huf", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "numbers-highlight", " " ))]/text()',MapCompose(str.strip),Join(),MapCompose(lambda i: i.replace(' ','')))
        l.add_xpath('adress1', './/*[contains(concat( " ", @class, " " ), concat( " ", "address-highlighted", " " ))]/text()')
        l.add_xpath('adress2', './/*[contains(concat( " ", @class, " " ), concat( " ", "zone-address", " " ))]/text()')
        l.add_xpath('adress3', './/*[contains(concat( " ", @class, " " ), concat( " ", "address", " " ))]/a/text()')
        l.add_xpath('lon', './@data-lon')
        l.add_xpath('lan', './@data-lan')
        l.add_xpath('date', './@data-ld')
        l.add_xpath('rentid', './@data-id')
        l.add_xpath('size', './/*[contains(concat( " ", @class, " " ), concat( " ", "centered", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "numbers-highlight", " " ))]/text()')
        l.add_xpath('rooms', './/*[contains(concat( " ", @class, " " ), concat( " ", "roomcount", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "numbers-highlight", " " ))]/text()')

        return l.load_item()
