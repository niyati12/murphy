from reverse_hash import Hash
from web_crawler import Crawler
from urlparse import Urlparse

def run_hash():
	hash_key = Hash('acdegilmnoprstuw')
	print hash_key.reverse_hash(680131659347)

def run_crawler():
	url = 'http://www.shopping.com'
	crawler = Crawler(driver,url)
	
	keyword = 'hair straighteners'
	page_no = 5

	print "total search results for ", keyword
	print extract_data(crawler, keyword)
	print "total search results for ", keyword, "and page number ", page_no
	print extract_data(crawler, keyword, page_no)

def run_urlparse():
	urlparse = Urlparse()
	print urlparse.parse_query('http://www.cwi.nl:80/%7Eguido/Python.com;a=123&b=12?name=xyz&name1=abc&relationship=friends')
