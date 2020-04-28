import scrapy
from scrapy_splash import SplashRequest

#This script takes all the input values for each country, (for examples: AU for Australia, GB for Great Britain)

class WsProjectItem(scrapy.Item):
    link_country = scrapy.Field() #This is the name of the item scrapped in this spider

class MySpider(scrapy.Spider):
    name = "link_country" #This is the name of the spider

    def start_requests(self):
        yield SplashRequest(
            url="https://openaq.org/#/locations?parameters=pm25&page=1&_k=u1wk8l", #This is the URL that will be scrapped
            callback= self.parse, 
            endpoint= 'render.html',
            args= {"wait": 5} #We shoul give 5 seconds to scrapy_splash to render the website
        )

    def parse(self, response):
        xpath = '//div[@class= "filters filters--country"]/div/div/div/label/input//@value'
        selection = response.xpath(xpath)
        a = []
        for s in selection:
            l = WsProjectItem()
            l['link_country'] = s.get()
            yield l
#In the shell it should be run: scrapy crawl link_country -o Data/Links/link_country.csv
