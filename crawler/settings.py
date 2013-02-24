import os
PROJECT_PATH = '/home/boat/workspace/code/minicrawler'
LIMIT = 10000

BOT_NAME = 'tuancrawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/11.10 Chromium/18.0.1025.168 Chrome/18.0.1025.168 Safari/535.19'
USER_AGENT_LIST = [
    "Googlebot/2.1 (+http://www.google.com/bot.html)",
    "Googlebot/2.2 (+http://www.google.com/bot.html)",
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/11.10 Chromium/18.0.1025.168 Chrome/18.0.1025.168 Safari/535.19',
    'Mozilla/5.0 (iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10'
    ]

DEFAULT_ITEM_CLASS = 'crawler.items.CrawlerItem'
ITEM_PIPELINES = ['crawler.pipelines.mongo_storage',]
EXTENSIONS = {
#    'scrapy.contrib.corestats.CoreStats': 500,
#    'crawler.statstodb.StatsToMongo': 1000,
    }
DOWNLOADER_MIDDLEWARES = {
#    'crawler.middlewares.UMDownloadMiddleware': 400,
#    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    }
REDIRECT_ENABLED = False
REDIRECT_MAX_TIMES =0 

MONGODB = {'host':'localhost','port':27017,'name':'test'}
MYSQLDB = {'host':'localhost','port':27017,'name':'test','user':'root','pwd':'root'}

MAIL_DEBUG = False
MAIL_HOST = 'mail.google.com'
MAIL_PORT = 25
MAIL_FROM = 'gongming@umeng.com'
MAIL_PASS = 'umeng123'
MAIL_USER = 'gongming@umeng.com'

COOKIES_ENABLED = True
DNSCACHE_ENABLED = True

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'cn',
}

PROXIES = [{'ip_port': 'xx.xx.xx.xx:xxxx', 'user_pass': 'foo:bar'},
           {'ip_port': 'PROXY2_IP:PORT_NUMBER', 'user_pass': 'username:password'},
           {'ip_port': 'PROXY3_IP:PORT_NUMBER', 'user_pass': ''},]
