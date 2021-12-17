import scrapy
from scrapy import Request
from amazon.config.asins import products, reviews_base_url
import re


def get_date_place(param):
    date_part, place = None, None
    if not param:
        date_part, place
    expression = r'([\w]+ \d+, \d+)'
    result = re.search(expression, param)
    if result:
        date_part = result.group(0)
        place = param.replace(date_part, '').replace('Reviewed in', '').replace('on', '').strip()
    return date_part, place


class ReviewsSpider(scrapy.Spider):
    name = 'reviews'

    def start_requests(self):
        for asin in products:
            yield Request(reviews_base_url.format(asin), meta={'asin': asin})

    def parse(self, response):
        asin = response.meta.get('asin')
        for review in response.css('#cm_cr-review_list [data-hook="review"]'):
            item = {}
            stars = review.css('[data-hook="review-star-rating"] ::text').get()
            stars = stars.replace('out of 5 stars', '').strip() if stars else None
            review_date_text = review.css('[data-hook="review-date"] ::text').get()
            date_part, place = get_date_place(review_date_text)
            item['ASIN'] = asin
            for att in review.xpath('.//a[@data-hook="format-strip"]/text()').getall():
                item[att.split(':')[0]] = att.split(':')[1]
            item['ProfileName'] = review.css('.a-profile-name ::text').get()
            item['Stars'] = stars
            item['StarsText'] = review.css('[data-hook="review-star-rating"] ::text').get()
            item['Title'] = review.css('[data-hook="review-title"] span ::text').get()
            item['ReviewDate'] = date_part
            item['ReviewedAt'] = place

            item['URL'] = response.url
            review_text = review.css('[data-hook="review-body"] span::text').getall()
            for i, text in enumerate(review_text):
                review_text[i] = text.strip('\n').strip('\r').strip('\t').strip()
            item['Review'] = '\n'.join(review_text)


            yield item

        next_page = response.xpath('//a[contains(text(),"Next page")]/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), meta={'asin': asin})
