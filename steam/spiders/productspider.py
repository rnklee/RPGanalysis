import logging

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
				allow = 'page=(d+)',
				restrict_css = '.search_pagination_right'
				)
			)
	]

	def parse_product(self, response):

		# Circumvent the age checkpoint issue
		if '/agecheck/app' in response.url:
			logger.debug(f"Form-type age check triggered for {response.url}.")

			form = response.css('#agegate_box form')

			action = form.xpath('@action').extract_first()
			name = form.xpath('input/@name').extract_first()
			value = form.xpath('input/@value').extract_first()

			formdata = {
				name: value,
				'ageDay': '23',
				'ageMonth': '10',
				'ageYear': '1977'
			}

			yield FormRequest(
				url = action,
				method = 'POST',
				formdata = formdata,
				callback = self.parse_product
			)

		else:
			yield self.load_product(response) 
			

	def load_product(self, response):
		loader = ProductLoader(item = ProductItem(), response = response)
		loader.add_css('name', '.apphub_AppName ::text')
		loader.add_css('price', 'div.discount_original_price ::text')
		loader.add_css('tags', 'a.app_tag ::text')

		return loader.load_item()