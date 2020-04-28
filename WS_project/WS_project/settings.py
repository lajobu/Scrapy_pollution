# -*- coding: utf-8 -*-

BOT_NAME = 'WS_project'

#To use scrapy_splash will should setup the below settings

SPIDER_MODULES = ['WS_project.spiders']
NEWSPIDER_MODULE = 'WS_project.spiders'

SPLASH_URL = 'http://localhost:8050/'
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

ROBOTSTXT_OBEY = True
