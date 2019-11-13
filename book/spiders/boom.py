# -*- coding: utf-8 -*-
import scrapy
from book.items import BookItem
from scrapy.http import Request
# from urllib import parse
import urlparse as parse

#-----------------
#爬取 排行榜  https://www.fpzw.com/top/ 下属子栏目  例 https://www.fpzw.com/top/dayvisit6_1.html（日排行榜 - 科幻 - 小说榜）
#----------------



class BoomSpider(scrapy.Spider):
    name = 'boom'
    allowed_domains = ['www.fpzw.com']
    start_urls = ['https://www.fpzw.com/top/dayvisit9_1.html']

    def parse(self, response):
        '''
        书籍信息 及 列表
        '''
        j=0
        for sel in response.xpath('//table[@class="sf-grid"]/tbody/tr'):
            j+=1
            if j > 2:
                #爬取多少本书，超出跳出
                break
            name = sel.xpath('./td[2]/a/text()').extract_first().strip()
            auther = sel.xpath('./td[6]/a/text()').extract_first().strip()
            link = sel.xpath('./td[2]/a/@href').extract_first().strip()
            time = sel.xpath('./td[7]/text()').extract_first().strip()
            types = sel.xpath('./td[1]/text()').extract_first().replace("[", '').replace("]", '')
            file_name = "[%s]%s-%s.txt" % (types,name,auther)
            desc = "[%s]%s      %s   \n%s      (%s)  \n" % (types,name,time,auther,link)
            yield scrapy.Request(link, callback=self.parse_list,meta={"file_name":file_name,"desc":desc})

    def parse_list(self, response):
        '''
        抓取章节url
        '''
        book = response.xpath('//dl/dt/h3/../following-sibling::dd')
        i = 0
        for sel in book:
            i += 1
            # if i > 2:
            #     break
            list_name = sel.xpath('./a/text()').extract_first().strip()
            list_url = parse.urljoin(response.url, sel.xpath('./a/@href').extract_first().strip())
            
            yield scrapy.Request(url=list_url, callback=self.parse_content, meta={'num': i, "list_name": list_name, "list_url": list_url,"file_name":response.meta['file_name'],"desc":response.meta['desc']})
    def parse_content(self, response):
        '''
        抓取章节内容
        '''
        arr = BookItem()
        arr['list_name'] = response.meta['list_name']
        arr['list_url'] = response.meta['list_url']
        arr['num'] = response.meta['num']
        arr['desc']= response.meta['desc']
        arr['file_name']= response.meta['file_name']
        title = response.xpath('//h2/text()').extract_first()
        content = response.xpath('//div[@id="box"]//p[@class="Text"]/text()').extract()
        arr['content'] = "\n".join(content)
        arr['title'] = title
        yield arr

