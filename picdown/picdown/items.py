# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class PicdownItem(Item):
    # define the fields for your item here like:
    # name = Field()
    #text = Field()
    image_urls = Field()
    image_paths = Field()
    site_url = Field()
    time = Field()
    text = Field()
    #link = Field()
    pass
