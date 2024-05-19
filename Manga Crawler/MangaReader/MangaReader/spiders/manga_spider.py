import scrapy

# scrapy crawl manga -o manga.json

class MangaLinkSpider(scrapy.Spider):
    name = "manga"
    start_urls = [
        "https://kissmanga.org/manga/manga-ny991307"
    ]
    
    
    def parse(self, response):
        #general info to pass as meta
        title = response.css("h2 strong.bigChar::text").get()
        author = response.css("p.info span::text").getall()
        genres = response.css("p.info span::text").getall()
        
        chapter_urls = []
        chapter_urls = response.css("h3 a::attr(href)").getall()
        
        for url in chapter_urls:
            yield scrapy.Request(response.urljoin(url), callback=self.parse_chapter, 
                                 meta={
                                        'title': title,
                                        'author': author,
                                        'genres': genres,
                                       })
        
    def parse_chapter(self, response):
        image_urls = response.css("div#centerDivVideo img::attr(src)").getall()
        chapter_number = response.css("select#selectEpisode option[selected]::text").get().strip()[-1]
        
        yield {
            response.meta['title']:
                {
                    "Chapter": chapter_number,
                    "Images": image_urls,
                    #"Author": response.meta['author'], #bugged extraction
                    #"Genres": response.meta['genres'], #bugged extraction

                }, 
        }
