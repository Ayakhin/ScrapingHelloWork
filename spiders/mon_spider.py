import scrapy
import time

class MonSpiderSpider(scrapy.Spider):
    name = "mon_spider"
    allowed_domains = ["www.hellowork.com"]
    start_urls = ["https://www.hellowork.com/fr-fr/"]
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 20  # Ajout d'un de 3 secondes entre chaque requête
    }

    def parse(self, response):
        extracted_text = response.css('h1.tw-inline-flex span::text').getall()
        extracted_text = ' '.join(extracted_text).strip().replace('\u202f', ' ')
        yield {'extracted_text': extracted_text}
