from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

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
        # Use the middleware methods here
        response = self.crawler.middlewares.get('MangareaderSpiderMiddleware').process_spider_input(response, self)
        # parsing code
        item = {}
        item['url'] = response.url
        return item