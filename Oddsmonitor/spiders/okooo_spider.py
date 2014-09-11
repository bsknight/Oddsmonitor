import scrapy

from Oddsmonitor.items import OddsmonitorItem

class OkoooSpider(scrapy.Spider):
	name = "okooo"
	allowed_domains = ["okooo.com"]
	start_urls = [
		"http://www.okooo.com/zucai/ren9/"
	]

	def parse(self, response):
		for sel in response.xpath('//div/table/tbody/tr'):
			item = OddsmonitorItem()
			item['name'] = sel.xpath('td[position() = 3]/a/p/span/text()').extract()
			#item['init_win'] = sel.xpath('td/span/text()').extract()
			yield item
