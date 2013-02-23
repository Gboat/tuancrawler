#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import urlparse
from md5 import md5

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.conf import settings
from scrapy.http import Request
from crawler.items import *

class Spider(CrawlSpider):
    '''
    get store info and tuangou info
    '''
    name = 'wowotuan'
    start_urls =[
            'http://weihai.55tuan.com/meishi',
            ]
    def parse(self,response):
        items = []
        hxs = HtmlXPathSelector(response)
        for url in list(set(hxs.selector("//a").re(".*store.*"))):
            yield Request(url,callback=parse)

        if re.match(ur".*store.*",response.url):
            items += parse_store(response)
        elif re.match(ur".*goods.*",response.url):
            items += parse_goods(response)

        for item in items:
            yield self.return_item(item)

    def return_item(self,item):
        return item

def parse_store(response):
    item = StoreItem()
    hxs = HtmlXPathSelector(response)

    return item

def parse_goods():
    item = TuanItem()
    hxs = HtmlXPathSelector(response)
    return item
