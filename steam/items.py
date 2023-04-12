# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader

class ProductItem(scrapy.Item):
    name = scrapy.Field()
    tags = scrapy.Field(
        output_processor = MapCompose(
            lambda x: x.replace('\r', '').replace('\n', '').replace('\t', '')
            )
        )
    num_reviews = scrapy.Field()    
    num_positive_reviews = scrapy.Field()
    url = scrapy.Field()

    release_month = scrapy.Field()
    release_day = scrapy.Field()
    release_year = scrapy.Field()


class ProductLoader(ItemLoader):
    default_output_processor = TakeFirst()

