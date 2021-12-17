# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class AmazonItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class AmazonProducts(scrapy.Item):
    asin = scrapy.Field()
    product_name = scrapy.Field()
    old_price = scrapy.Field()
    current_price = scrapy.Field()
    deal_price = scrapy.Field()
    category = scrapy.Field()
    product_availability = scrapy.Field()
