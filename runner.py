import scraper_helper as sh
from amazon.spiders.products import ProductsSpider
# from amazon.spiders.reviews_asin import ReviewsSpider
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    import time
    start_time = time.time()

    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(ProductsSpider)
    process.start()
    print("\n\n{:.2f} Seconds".format(time.time() - start_time))
