import scrapy

# scrapy crawl manga -o manga.json

class MangaLinkSpider(scrapy.Spider):
    name = "manga"
    start_urls = [
        "https://kissmanga.org/manga/manga-ny991307"
    ]
    
    def parse(self, response):
        chapter_urls = []
        # for chapter in response.css("h3 a"):
        #     urls.append(chapter.css("::attr(href)").get())
        chapter_urls = response.css("h3 a::attr(href)").getall()
        for url in chapter_urls:
            yield scrapy.Request(response.urljoin(url), callback=self.parse_chapter)
        
    def parse_chapter(self, response):
        image_urls = response.css("div#centerDivVideo img::attr(src)").getall()
        chapter_number = response.css("select#selectEpisode option[selected]::text").get().strip()[-1]
        yield {
            "Chapter_number": chapter_number,
            "image_urls": image_urls,
        }
