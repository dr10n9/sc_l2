# -*- coding: utf-8 -*-
import scrapy

class ForumMessagesSpider(scrapy.Spider):

    name = 'myNewSpider'
    allowed_domains = ['alltransua.com']
    #start_urls = ['http://alltransua.com/forum/forum.php?path=23']
    start_urls = ['http://alltransua.com/forum/topic.php?path=23&all=1']

    def parseMessages(self, response):
        self.log('scrapping forum...' + response.url)
        yield{

            # 'author_name': response_css('font::text').extract_first(),
            # 'text': response_css()
            # 'date':
            # 'topic_title':
        }
