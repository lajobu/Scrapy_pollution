# Scrapy_pollution

Here you can find my first web scraping project.

## Data analysis results:

* **Pollution level in PM2.5:**

![alt text](https://github.com/lajobu/Scrapy_pollution/blob/master/pollution_european_countries.2020-04-25%2012.15.png)

More details: https://github.com/lajobu/Scrapy_pollution/blob/master/Analysis.py

# What is web scraping?

* Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites Web scraping software may access the World Wide Web directly using the Hypertext Transfer Protocol, or through a web browser. While web scraping can be done manually by a software user, the term typically refers to automated processes implemented using a bot or web crawler. It is a form of copying, in which specific data is gathered and copied from the web, typically into a central local database or spreadsheet, for later retrieval or analysis. 

Source: [Wikipedia](https://en.wikipedia.org/wiki/Web_scraping)

## Details:

* **Website:** https://openaq.org/
* **Code languague:** Python3
* **Scraper:** scrapy
* **Libraries:** Numpy, Pandas, Seaborn, and Matplotlib
* **Adittional tools:** docker and scrapy_splah

## User manual:

### 1) Spider to be run: link_country
* $ scrapy crawl link_country -o Data/Links/link_country.csv
* It generates [link_country.csv](https://github.com/lajobu/Scrapy_pollution/blob/master/WS_project/Data/Links/link_country.csv), script: [link_country.py](https://github.com/lajobu/Scrapy_pollution/blob/master/WS_project/WS_project/spiders/link_country.py)

### 2) Spider to be run: pages
* $ scrapy crawl pages -o Data/Links/pages.csv
* It generates [pages.csv](https://github.com/lajobu/Scrapy_pollution/blob/master/WS_project/Data/Links/pages.csv), script: [pages.py](https://github.com/lajobu/Scrapy_pollution/blob/master/WS_project/WS_project/spiders/pages.py)

### 3) Spider to be run: pollution
* $ scrapy crawl pollution -o Data/pollution.csv
* It generates [pollution.csv](https://github.com/lajobu/Scrapy_pollution/blob/master/WS_project/Data/pollution.csv), script: [pollution.py](https://github.com/lajobu/Scrapy_pollution/blob/master/WS_project/WS_project/spiders/pollution.py)

### 4) Python script to be run: Analysis.py
* $ python3 Analysis.py - [Analysis.py](https://github.com/lajobu/Scrapy_pollution/blob/master/Analysis.py)
* It generates [result_pollution.csv](https://github.com/lajobu/Scrapy_pollution/blob/master/result_pollution.csv) and [pollution_european_countries.DATE.png](https://github.com/lajobu/Scrapy_pollution/blob/master/pollution_european_countries.2020-04-25%2012.15.png)
