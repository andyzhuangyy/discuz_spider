from scrapy.spider import Spider, BaseSpider
from scrapy.http import FormRequest, Request
from scrapy.selector import Selector

from picdown.items import PicdownItem

import scrapy
import picdown.config as config


cfgdict = config.src_dict[config.MY_PIC_SITE]


class MayaSpider(BaseSpider):
    name = "maya"
    allowed_domains = [cfgdict['domain']]
    #start_urls = [cur_dict['url']]

    def start_requests(self):
        return [Request(cfgdict['login_url'], callback=self.login)]
        

    def login(self, response):
        return FormRequest.from_response(
            response,
            formdata = cfgdict['login_form'],
            callback = self.after_login
            )

    def after_login(self, response):
        print 'after login'
        print response.headers
        self.xsrf = response.headers['Set-Cookie'].split(';')[0].split('=')[-1]
        print self.xsrf
        #wd = open('tmpbody.html', 'w+')
        #wd.write(response.body)
        #wd.close()
        requests = []
        for url in cfgdict['urls']:
            #urlsplit = cfgdict['login_url'].split('/')[:-1] 
            #urlsplit.append(url)
            #pageurl = '/'.join(urlsplit)
            pageurl = '/'.join(cfgdict['login_url'].split('/')[:-1] + [url])
            self.log('page list links: %s'%pageurl)
            yield Request(pageurl, callback=self.parse_piclistpage)


    def parse_piclistpage(self, response):
        sel = Selector(response)
        #print 'parse_piclistpage: ', response.body
        urls = sel.xpath(cfgdict['picpage_xpath']).extract()
        #wd = open('tmpbody.html', 'w+')
        #wd.write(response.body)
        #wd.close()
        for url in urls:
            pageurl = '/'.join(cfgdict['login_url'].split('/')[:-1] + [url])
            self.log('page links: %s'%pageurl)
            yield Request(pageurl, callback=self.parse)
        

    def parse(self, response):
        sel = Selector(response)
        item = PicdownItem()

        item['site_url'] = response.url
        #item['time'] = response_sel.xpath(cur_dict['time_xpath']).extract()[:1]
        item['text'] = sel.xpath(cfgdict['text_xpath']).extract()
        self.log('text : %s'%item['text'])
        image_urls = []
        links = sel.xpath(cfgdict['pic_xpath']).extract()
        for i, pic in enumerate(links):
            self.log('pic %d, links: %s'%(i+1, pic))
            image_urls.append(pic)
        item['image_urls'] = image_urls
        yield item


