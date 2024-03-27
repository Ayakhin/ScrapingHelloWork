import scrapy


class MonSpiderSpider(scrapy.Spider):
    name = "mon_spider"
    allowed_domains = ["www.hellowork.com"]
    start_urls = ["https://www.hellowork.com/fr-fr/"]

    def parse(self, response):
        extracted_text = response.css('h1.tw-inline-flex span::text').getall()
        extracted_text = ' '.join(extracted_text).strip()
        yield {'extracted_text': extracted_text}
