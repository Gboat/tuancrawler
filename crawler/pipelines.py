import pymongo
from datetime import datetime
from scrapy.exceptions import DropItem
from scrapy import log
from crawler.settings import MONGODB

class mongo_storage(object):
    def __init__(self):
        connection = pymongo.Connection(MONGODB['host'],MONGODB['port'])
        self.db = connection[MONGODB['name']]
        self.date = datetime.now().strftime("%Y-%m-%d")
    def create_index(self):
        db.appmeta.ensure_index({"md5":1},name="appmeta_key")
        db.marketmeta.ensure_index({"marketmeta":1},name="appmeta_key")
                                     
    def process_item(self, item, spider):
        if 'TuanItem' == item.__class__.__name__:
            self.process_tuan_item(item)
        elif 'StoreItem' == item.__class__.__name__:
            self.process_store_item(item)
        else:
            raise DropItem("Unknown Item Type !!!")
        return item
    def process_tuan_item(self,item):
        pass

    def process_store_item(self,item):
        pass
