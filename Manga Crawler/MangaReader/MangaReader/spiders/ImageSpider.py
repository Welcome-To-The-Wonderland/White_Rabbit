from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Command: 
# scrapy crawl mycrawler -o output.txt

class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["kissmanga.org"]
    start_urls = ["https://kissmanga.org/manga/manga-ny991307"]

    rules = (
        Rule(LinkExtractor(allow="chapter/manga-ny991307/"), callback='parse_item'),
    )

    def parse_item(self, response):
        # parsing code goes here
        pass