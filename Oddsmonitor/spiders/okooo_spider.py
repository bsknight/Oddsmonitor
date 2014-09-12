import scrapy

from Oddsmonitor.items import GameItem
from Oddsmonitor.items import OddsItem

class OkoooSpider(scrapy.Spider):
    name = "okooo"
    allowed_domains = ["okooo.com"]
    start_urls = [
        "http://www.okooo.com/zucai/ren9/"
    ]

    def parse(self, response):
        i = 1
        for sel in response.xpath('//div/table/tbody/tr'):
            item = GameItem()
            
            temp = '//div[@id="gametablesend"]/table/tbody/tr['+ str(i) +']/td[4]/a[@class="sbg"]/span[@class="homenameobj homename"]/text()'
            gameName = sel.xpath(temp).extract()[0]
            
            temp = '//div[@id="gametablesend"]/table/tbody/tr['+ str(i) +']/td[4]/a[@class="fbg"]/span[@class="awaynameobj awayname"]/text()'
            gameName += ' vs ' + sel.xpath(temp).extract()[0]           
            
            temp = '//div[@id="gametablesend"]/table/tbody/tr['+ str(i) +']/td[7]/a[@class="jsOupei"]/@href'
            item['link'] = 'http://www.okooo.com'+ sel.xpath(temp).extract()[0]
            
            item['name'] = gameName
            
            yield item
            i = i + 1
