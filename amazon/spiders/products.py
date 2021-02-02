import scrapy
from amazon.items import AmazonProducts

class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ["amazon.com"]
  
    #Use working product URL below
    start_urls = [
        "http://www.amazon.com/dp/B0046UR4F4",
        "http://www.amazon.com/dp/B00JGTVU5A",
        "http://www.amazon.com/dp/B00O9A48N2",
         "http://www.amazon.com/dp/B00UZKG8QU"
        ]

    def parse(self, response):
        items = AmazonProducts()
        title = response.xpath('//h1[@id="title"]/span/text()').extract()
        sale_price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
        category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
        availability = response.xpath('//div[@id="availability"]//text()').extract()
        items['product_name'] = ''.join(title).strip()
        items['product_sale_price'] = ''.join(sale_price).strip()
        items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
        items['product_availability'] = ''.join(availability).strip()
        yield items