# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import log

class PicdownPipeline(object):
    def process_item(self, item, spider):
        print 'process_item'
        return item

class MyimagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print 'get_media_requests'
        for image_url in item['image_urls']:
            #image_url +='?filepre=' + item['time'][0] + '-' + '-'.join(item['text'])
            log.msg('image: ' + image_url, level=log.INFO)
            yield scrapy.http.Request(image_url)

    def item_completed(self, results, item, info):
        print 'result: ', results
        print 'item: ', item
        print 'info: ', dir(info)
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

