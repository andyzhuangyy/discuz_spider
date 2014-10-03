# Scrapy settings for picdown project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import config

BOT_NAME = 'picdown'

SPIDER_MODULES = ['picdown.spiders']
NEWSPIDER_MODULE = 'picdown.spiders'
ITEM_PIPELINES = {
    'picdown.pipelines.MyimagePipeline': 1,
    'picdown.pipelines.PicdownPipeline': 10,
}

IMAGES_STORE = '../pic/' + config.MY_PIC_SITE

#90 days expires
IMAGES_EXPIRES = 90



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'picdown (+http://www.yourdomain.com)'
