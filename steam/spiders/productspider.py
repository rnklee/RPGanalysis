import logging
import re
import pdb

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import FormRequest

from steam.items import ProductItem, ProductLoader 


logger = logging.getLogger(__name__)

class ProductSpider(CrawlSpider):
	name = 'productspider'
	# category1=998 to search exclusively for games (not DLCs/soundtrackls/etc).
	start_urls = ['https://store.steampowered.com/search/?category1=998&filter=topsellers']

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

			sessionID = response.xpath('//script[contains(.,"g_sessionID = ")]/text()').extract()[0]
			sessionID = re.findall('g_sessionID = (.+?);', sessionID)[0]

			formdata = {
				'sessionID': sessionID,
				'ageDay': '23',
				'ageMonth': '10',
				'ageYear': '1977'
			}

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

		no_discount_price = response.css('div.game_purchase_price ::text').extract_first() # returns price when the game is not on sale and there's no discount_original_price.	
		discount_price = response.css('div.discount_original_price ::text').extract_first() # despite its name should return the original price if the game's currently on sale.
		price = no_discount_price or discount_price
		#pdb.set_trace()

		if not price:
			logger.debug(f'No price found for {response.url}.')
		if '$' not in price:
			price = '$0.00' 
		price = re.findall(r'\$[0-9]*\.[0-9]{2}', price)[0]
		loader.add_value('price', price)
		loader.add_css('tags', 'a.app_tag ::text')

		return loader.load_item()