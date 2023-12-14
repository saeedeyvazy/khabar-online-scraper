from pathlib import Path

import scrapy


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
        text_list=""
        
        if len(video) != 0 :
            file =  video.get()
            result = 'STARTP ' + response.css('p.summary::text').get()
        else:
            text_list = response.css('div.item-text p::text')
            result = 'STARTP' + '،'.join(text_list[1].get().split('،')[1:]) + "\n\n"
            file = response.css('figure.item-img img::attr(src)').get()

            for i in range(2, len(text_list) - 1) :
                result += 'STARTP' + text_list[i].get() + "\n\n"
            
        yield{'title' : title, 'text' : result, 'file':file, 'url':response.request.url}

        