import scrapy
from scrapy.spiders import CrawlSpider
import xpath
from spyder.spyder.items import SpyderItem


class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            yield ({
                'text': quote.xpath("span[@class='text']/text()").get(),
                'author': quote.xpath("span/small/text()").extract(),
                'author-link': quote.xpath("a/@href").get(),
                'tags': quote.xpath("div[@class='tags']/a/text()").extract()
            })
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0]+next_link)
