import scrapy
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser

from amazon.config.asins import products, products_base_url
from scrapy import Request
import scraper_helper as sh
import price_parser
from amazon.items import AmazonProducts


class ProductsSpider(scrapy.Spider):
    name = 'products'
    ransom_user_agent = True

    def start_requests(self):
        for product in products:
            yield Request(products_base_url.format(product['asin']),
                          cb_kwargs={
                              'asin': product['asin']
                          })

    def parse(self, response, asin):
        open_in_browser(response)
        item = AmazonProducts()
        product_name = response.xpath('normalize-space(//h1[@id="title"]/span/text())').get()
        old_price = response.xpath(
            'normalize-space(//span[@class="priceBlockStrikePriceString a-text-strike"]/text())').get()
        if old_price:
            old_price = price_parser.parse_price(old_price).amount_float
        current_price = response.xpath('normalize-space(//span[@id="priceblock_ourprice"]/text())').get()
        if current_price:
            current_price = price_parser.parse_price(current_price).amount_float
        deal_price = response.xpath('normalize-space(//span[@id="priceblock_dealprice"]/text())').get()
        if deal_price:
            deal_price = price_parser.parse_price(deal_price).amount_float
        # categories = response.xpath(
        #     '//div[@id="wayfinding-breadcrumbs_container"]//span[@class="a-list-item"]/a/text()').getall()
        availability = response.xpath('normalize-space(//div[@id="availability"]/span/text())').get()
        item['asin'] = str(asin)
        item['product_name'] = product_name
        item['old_price'] = old_price
        item['current_price'] = current_price
        item['deal_price'] = deal_price
        # item['category'] = ' > '.join(map(lambda x: sh.cleanup(x), categories))
        item['category'] = 'NA'
        item['product_availability'] = ''.join(availability).strip()
        yield item

