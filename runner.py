import scraper_helper as sh
# from amazon.spiders.review_asin import ReviewsSpider
from amazon.spiders.reviews_asin import ReviewsSpider
import scrapy

if __name__ == '__main__':
    import time
    start_time = time.time()
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(ReviewsSpider)
    process.start()
    print("\n\n{:.2f} Seconds".format(time.time() - start_time))
