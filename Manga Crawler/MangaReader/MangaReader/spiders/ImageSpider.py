from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Item, Field

# https://docs.scrapy.org/en/latest/intro/overview.html

# Command: 
# scrapy crawl mycrawler -o output.json

class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["kissmanga.org"] 
    start_urls = ["https://kissmanga.org/manga/manga-ny991307"]

    rules = (
        Rule(LinkExtractor(allow="chapter/manga-ny991307/"), callback='parse_item'),
    )

    def parse_item(self, response):
        series = response.url.split('/')[4].split('-')[1]
        chapter_number = response.url[-1]
        item = {}
        item[series] = [{chapter_number: response.url}]
        return item