from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# https://kissmanga.org/manga/manga-ny991307

class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["kissmanga.org"]
    start_urls = ["https://kissmanga.org/manga/manga-ny991307"]

    rules = (
        Rule(LinkExtractor(allow="chapter/manga-ny991307/")),
    )