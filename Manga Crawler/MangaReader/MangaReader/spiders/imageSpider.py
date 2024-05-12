from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# https://docs.scrapy.org/en/latest/intro/overview.html

# Command: 
# scrapy crawl imageCrawler -o images.json

class CrawlingSpider(CrawlSpider):  
    name = "imageCrawler"
    allowed_domains = ["kissmanga.org"] 
    start_urls = ["https://kissmanga.org/chapter/manga-ny991307/chapter-9"]
    base_url = "https://kissmanga.org/chapter/manga-ny991307/chapter-9" #change to input based later
    # https://cm.blazefast.co
    rules = (
        Rule(LinkExtractor(allow=base_url), callback='parse_item'),
    )
    
    def parse_item(self, response):
        image_urls = response.css('#centerDivVideo img::attr(src)').getall()
        item = {}
        item['image_urls'] = image_urls
        return item
        