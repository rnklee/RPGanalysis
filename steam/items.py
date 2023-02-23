# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader

class ProductItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    tags = scrapy.Field(
        output_processor = MapCompose(
            lambda x: x.replace('\r', '').replace('\n', '').replace('\t', '')
            )
        )


class ProductLoader(ItemLoader):
    default_output_processor = TakeFirst()

