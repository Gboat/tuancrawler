#coding:utf-8
from scrapy.item import Item, Field

class CrawlerItem(Item):
    pass
class TuanItem(Item):
    date = Field()
    market = Field()
    title = Field()
    price = Field()
    content = Field()
    store = Field()

    def __str__(self):
        return ("TuanItem:%s"%(self['title']))

class StoreItem(Item):
    market = Field()
    store = Field()
    name = Field()
    desc = Field()
    place = Field()

    def __str__(self):
        return ("StoreItem:%s"%(self['name']))
