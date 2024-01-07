from pathlib import Path

import scrapy
import logging

logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s] {%(name)s} %(levelname)s:  %(message)s', 
                    datefmt='%y-%m-%d %H:%M:%S', 
                    filename="khabar-online.log",
                    ) 
logger = logging.getLogger('KHABAR_ONLINE_LOGGER') 

class QuotesSpider(scrapy.Spider):
    name = "khabaronline"

    allowed_domains = ["www.khabaronline.ir"]
    start_urls = ["https://www.khabaronline.ir/"]
    
    def parse(self, response):
        news_link_list = response.css('#box5 a::attr(href)')
        for link in news_link_list:
            print(link.get())
            yield response.follow(link.get(), callback=self.parse_fetched_link)

    def parse_fetched_link(self, response):
        title = response.css('h1.title a::text').get()
        video = response.css('video source::attr(src)')
        file=""
        summary = response.css('p.summary::text').get()
        title = title.replace('ببینید |','',1)
        result = 'STARTP ' + summary + '\n'
        
        if len(video) != 0 :
            file =  video.get()
            yield{'title' : title, 'text' : result, 'file':file, 'url':response.request.url}
        # else:
        #     text_list = response.xpath('/html/body/main/div/div[1]/div[1]/article/div[3]/p//text()').getall()
        #     result = 'STARTP' + text_list[0] + "\n\n"
        #     file = response.css('figure.item-img img::attr(src)').get()

        # else:
            
        #     result += 'STARTP' + ' '.join(response.xpath('/html/body/main/div/div[1]/div[1]/article/div[4]/div[1]/p[1]//text()').getall()) + '\n'

        #     file = response.css('figure.item-img img::attr(src)').get()
        #     bottomFileList = response.xpath('/html/body/main/div/div[1]/div[1]/article/div[4]/div[1]/p/img/@src').getall()
        #     if bottomFileList != None:
        #          for item in bottomFileList:
        #              file += "$$" + item
                
        

        