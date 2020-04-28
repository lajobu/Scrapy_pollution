import scrapy
from scrapy_splash import SplashRequest
import pandas as pd

#This script takes all the output values from the spider link_country, the output are the links of each page

df = pd.read_csv(
    'WS_project/Data/Links/link_country.csv') #To read the output from the spider link_country
a = df.values.tolist()
b = []
for i in range(len(a)): 
    b.append('https://openaq.org/#/locations?page=1&countries=' +
             str((', '.join(a[i]))) + '&parameters=pm25') #It will be joined to the base URL

c = []
for i in range(len(b)):
    b.append(str(', '.join(b[i])))
c

class WsProjectItem(scrapy.Item):
    link = scrapy.Field()

class MySpider(scrapy.Spider):
    name = "pages"
    start_urls = []

    def start_requests(self):
        urls = b #We will go to the each base URL created before
        for url in urls:
            yield SplashRequest(
                url,
                callback=self.parse,
                endpoint='render.html',
                args={"wait": 8},
        )

    def parse(self, response):
        xpath = '//article[@class= "card card--data"]/div/header/div/h1/a//@href' #We will take the href link
        selection = response.xpath(xpath)
        for s in selection:
            l = WsProjectItem()
            l['link'] = 'https://openaq.org/' + s.get() #As output it will be joined to the base URL
            yield l

#In the shell it should be run: scrapy crawl pages -o Data/Links/pages.csv

#After that, we will obtain all the URLS for each country and station (only for the first page)