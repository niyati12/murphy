#import modules
from selenium import webdriver
import re
import time

class Crawler:
	def __init__(self,driver,url):
		self.driver = webdriver.Firefox()
		self.driver.get(url)

#function to get total number of search results given a keyword and/or page number
def extract_data(crawler, keyword, page_no=None):
	#if total results count has to be returned
	if page_no is None:
		search = crawler.driver.find_element_by_id('searchBarTxtField')
		search.clear()
		search.send_keys(keyword)
		button = crawler.driver.find_element_by_id('searchSubmitBtn')
		button.click()
		time.sleep(15)
		total_results = crawler.driver.find_element_by_class_name('numTotalResults')
		total_results = str(total_results.text).split(' ')
		total_results = total_results[len(total_results)-1]
		try:
			total_results = int(total_results)
		except ValueError:
			try:
				total_results = int(total_results[:len(total_results)-1])
			except ValueError:
				total_results = 0
	#if specific page's result count has to be returned
	else:
		page_no = 'PL' + str(page_no)
		pagination_elements = crawler.driver.find_element_by_css_selector\
		('#centerPanel > div.centerInnerPanel > div:nth-child(3) > div.paginationNew > span:nth-child(2)')
		pagination_links = pagination_elements.find_elements_by_tag_name('a')

		flag = False
		for link in pagination_links:
			if link.get_attribute('name') == page_no:
				flag = True
				link.click()
				break
		if flag == False:
			print "Page number does not exist"
			return 0
		time.sleep(15)
		total_results = crawler.driver.find_element_by_class_name('numTotalResults').text

		nums = re.findall('\d+',total_results)
		if nums:
			try:
				total_results = int(nums[1]) - int(nums[0]) + 1
			except IndexError:
				total_results = 0
	return total_results

#driver program

if __name__ == '__main__':
	url = 'http://www.shopping.com'
	crawler = Crawler(driver,url)
	
	keyword = 'hair straighteners'
	page_no = 5

	print "total search results for ", keyword
	print extract_data(crawler, keyword)
	print "total search results for ", keyword, "and page number ", page_no
	print extract_data(crawler, keyword, page_no)