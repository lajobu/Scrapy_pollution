# Scrapy_pollution

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Here you can find my first `web scraping project`.

## :star: Data analysis results:

* **Pollution level in PM2.5:**

![alt text](https://github.com/lajobu/Scrapy_pollution/blob/master/pollution_european_countries.2020-04-25%2012.15.png)

 :link: More details: https://github.com/lajobu/Scrapy_pollution/blob/master/Analysis.py

## :star: Details:

:round_pushpin: **Website:** https://openaq.org/

:round_pushpin: **Code languague:** Python3

:round_pushpin: **Scraper:** scrapy

:round_pushpin: **Libraries:** Numpy, Pandas  :panda_face:, Seaborn  :bar_chart:, and Matplotlib

:round_pushpin: **Adittional tools:** docker and scrapy_splah

#  :question: What is web scraping?

Web scraping, web harvesting, or web data extraction is data scraping used for `extracting data from websites` Web scraping software may access the World Wide Web directly using the Hypertext Transfer Protocol, or through a web browser. While web scraping can be done manually by a software user, the term typically refers to `automated processes implemented using a bot or web crawler`. It is a form of copying, in which specific data is gathered and copied from the web, typically into a central local database or spreadsheet, for later retrieval or analysis. 

Source:  :link: [Wikipedia](https://en.wikipedia.org/wiki/Web_scraping)

## :star: User manual:

### :ballot_box_with_check: 1) Spider to be run: link_country
* $ scrapy crawl link_country -o Data/Links/link_country.csv
* It generates  :link: [link_country.csv](https://github.com/lajobu/Scrapy_pollution/blob/master/WS_project/Data/Links/link_country.csv), script:  :link:  [link_country.py](https://github.com/lajobu/Scrapy_pollution/blob/master/WS_project/WS_project/spiders/link_country.py)

### :ballot_box_with_check: 2) Spider to be run: pages
* $ scrapy crawl pages -o Data/Links/pages.csv
* It generates  :link: [pages.csv](https://github.com/lajobu/Scrapy_pollution/blob/master/WS_project/Data/Links/pages.csv), script:  :link: [pages.py](https://github.com/lajobu/Scrapy_pollution/blob/master/WS_project/WS_project/spiders/pages.py)

### :ballot_box_with_check: 3) Spider to be run: pollution
* $ scrapy crawl pollution -o Data/pollution.csv
* It generates  :link: [pollution.csv](https://github.com/lajobu/Scrapy_pollution/blob/master/WS_project/Data/pollution.csv), script:  :link: [pollution.py](https://github.com/lajobu/Scrapy_pollution/blob/master/WS_project/WS_project/spiders/pollution.py)

### :ballot_box_with_check: 4) Python script to be run: Analysis.py
* $ python3 Analysis.py -  :link: [Analysis.py](https://github.com/lajobu/Scrapy_pollution/blob/master/Analysis.py)
* It generates  :link: [result_pollution.csv](https://github.com/lajobu/Scrapy_pollution/blob/master/result_pollution.csv) and  :link:  [pollution_european_countries.DATE.png](https://github.com/lajobu/Scrapy_pollution/blob/master/pollution_european_countries.2020-04-25%2012.15.png)
