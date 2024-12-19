# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


def convertPrice(price):
    print('convertPrice')
    print('convertPrice')
    print('price',price)
    print('convertPrice')
    print('convertPrice')
    return f'covertPrice-{price}'
class FlipkartItem(scrapy.Item):
    title = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, convertPrice),
        output_processor=TakeFirst(),
    )