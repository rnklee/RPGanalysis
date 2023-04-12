import logging
import pdb

import re
import datetime

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import FormRequest

from steam.items import ProductItem, ProductLoader 


logger = logging.getLogger(__name__)

class ProductSpider(CrawlSpider):
	name = 'productspider'
	# category1=998 to search exclusively for games (not DLCs/soundtrackls/etc).
	# sort_by=Released_DESC to search exclusively for released games.
	# tags=122 for RPGs.
	start_urls = ['https://store.steampowered.com/search/?sort_by=Released_DESC&tags=122&category1=998&supportedlang=english']

	allowed_domains = ['steampowered.com']
	rules = [
		Rule(
			LinkExtractor(
				allow = '/app/(.+)/',
				restrict_css = '#search_result_container'
				),
			callback = 'parse_product'
			),
		Rule(
			LinkExtractor(
				allow = 'page=',
				restrict_css = '.search_pagination_right'
				)
			)
	]

	def parse_product(self, response):

		# Circumvent the age checkpoint issue
		if '/agecheck/app' in response.url:
			logger.debug(f"Form-type age check triggered for {response.url}.")

			app_number = re.findall('/[0-9]+/', response.url)[0]
			app_number = app_number.replace('/', '')
			url = 'https://store.steampowered.com/app/' + app_number

			yield FormRequest(
				url = url, 
				callback = self.parse_product,
				cookies = {'wants_mature_content':'1'})
		else:
			yield self.load_product(response) 
			

	def load_product(self, response):
		loader = ProductLoader(item = ProductItem(), response = response)
		loader.add_css('name', '.apphub_AppName ::text')
		loader.add_css('tags', 'a.app_tag ::text')
		loader.add_xpath('num_reviews', '//input[@id="review_summary_num_reviews"]/@value')
		loader.add_xpath('num_positive_reviews', '//input[@id="review_summary_num_positive_reviews"]/@value')		
		loader.add_value('url', response.url)

		#pdb.set_trace()
		release_date = response.xpath('//div[@class="release_date"]/div[@class="date"]/text()').extract_first()
		release_date = datetime.datetime.strptime(release_date, '%b %d, %Y')
		loader.add_value('release_month', release_date.month)
		loader.add_value('release_day', release_date.day)
		loader.add_value('release_year', release_date.year)		

		return loader.load_item()