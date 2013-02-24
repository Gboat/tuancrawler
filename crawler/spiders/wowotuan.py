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
            #'http://weihai.55tuan.com/meishi',
            'http://weihai.55tuan.com/meishi-0-0-0-0-0-0-1',
            ]
    def parse(self,response):
        items = []
        hxs = HtmlXPathSelector(response)
        if re.match(ur".*store.*",response.url):
            items += parse_store(response)
        elif re.match(ur".*goods.*",response.url):
            items += parse_goods(response)
        else :
            for url in list(set(hxs.select("//a/@href").re(".*store.*"))):
                yield Request(url,callback=self.parse)

            for url in list(set(hxs.select("//a/@href").re(".*goods.*"))):
                yield Request(url,callback=self.parse)

        for item in items:
            yield self.return_item(item)

    def return_item(self,item):
        return item

def parse_store(response):
    items = []
    hxs = HtmlXPathSelector(response)

    item = StoreItem()
    item['store'] = ""
    item['market'] = ""
    item['name'] = ""
    item['place'] = ""
    item['desc'] = ""

    items.append(item)
    return items

def parse_goods(response):
    items = []
    hxs = HtmlXPathSelector(response)

    item = TuanItem()
    item['title'] = "" 
    item['content'] = ""
    item['market'] = ""
    item['store'] = ""
    item['date'] = ""

    items.append(item)
    return items
