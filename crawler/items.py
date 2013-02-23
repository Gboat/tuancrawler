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
    place = Field()
    store = Field()
    def __str__(self):
        return ("TuanItem:%s"%(self['title']))

 
class StoreItem(Item):
    name = Field()
    desc = Field()
    def __str__(self):
        return ("StoreItem:%s"%(self['name']))

 
