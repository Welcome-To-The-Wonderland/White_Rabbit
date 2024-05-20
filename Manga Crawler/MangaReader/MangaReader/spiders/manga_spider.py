import scrapy
import re
import os

# scrapy crawl manga -o manga.json

class MangaLinkSpider(scrapy.Spider):
    name = "manga"
    
    # delete old json file data if it exists
    def __init__(self, *args, **kwargs):
        super(MangaLinkSpider, self).__init__(*args, **kwargs)
        if os.path.exists("manga.json"):
            os.remove("manga.json")
    
    start_urls = [
        #"https://kissmanga.org/manga/manga-ny991307"
        "https://kissmanga.org/manga/manga-ln951470"
    ]
    
    
    def parse(self, response):
        #general info to pass as meta
        title = response.css("h2 strong.bigChar::text").get()
        author = response.css("p.info span::text").getall() # bug, white space bullshit. Maybe use .strip()
        genres = response.css("p.info span::text").getall() # bug, white space bullshit. Maybe use .strip()
        chapter_urls = []
        chapter_urls = response.css("h3 a::attr(href)").getall()
        
        for url in chapter_urls:
            chapter_number = re.findall(r'\d+\.?\d*$', url)[0]
            yield scrapy.Request(response.urljoin(url), callback=self.parse_chapter, 
                                 meta={
                                        'title': title,
                                        'author': author,
                                        'genres': genres,
                                        'chapter' : chapter_number
                                       })
        
    def parse_chapter(self, response):
        image_urls = response.css("div#centerDivVideo img::attr(src)").getall()
        yield {
            response.meta['title']:
                {
                    "Chapter": response.meta['chapter'],
                    "Images": image_urls,
                    #"Author": response.meta['author'], #bugged extraction
                    #"Genres": response.meta['genres'], #bugged extraction
                }, 
        }
