from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# https://docs.scrapy.org/en/latest/intro/overview.html

# Command: 
# scrapy crawl linkCrawler -o output.json

class CrawlingSpider(CrawlSpider):
    name = "linkCrawler"
    allowed_domains = ["kissmanga.org"] 
    start_urls = ["https://kissmanga.org/manga/manga-ny991307"]
    base_url = "chapter/manga-ny991307/" #change to input based later

    rules = (
        Rule(LinkExtractor(allow=base_url), callback='parse_item'),
    )

    def parse_item(self, response):
        series = response.url.split('/')[4].split('-')[1]
        chapter_number = response.url[-1]
        item = {}
        item[series] = [{chapter_number: response.url}]
        return item