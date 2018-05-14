import re
class Urlparse:
	def parse_url(self,url):
		urlparse = {}
		arr_url = url.split('/')
		try:
			scheme = re.findall("(.*?):",url)[0]
		except IndexError:
			scheme = ''
		try:
			netloc = arr_url[2]
		except IndexError:
			netloc = ''
		try:
			port = int(netloc[netloc.index(':')+1:])
		except (IndexError, ValueError):
			port = None

		domain = arr_url[len(arr_url)-1]
		try:
			query = url.split('?')[1]
		except IndexError:
			query = ''

		try:
			index1 = url.index(';')
			index2 = url.index('?')
			params = url[index1+1:index2]
		except IndexError:
			params = ''

		urlparse['scheme'] = scheme
		urlparse['netloc'] = netloc
		urlparse['port'] = port
		urlparse['domain'] = domain
		urlparse['query'] = query
		urlparse['params'] = params
		return urlparse

	def parse_query(self,url):
		query = {}
		arr_url = url.split('?')[1].split('&')
		for q in arr_url:
			q = q.split('=')
			if q[0] in query.keys():
				query[q[0]].append(q[1])
			else:
				query[q[0]] = [q[1]]
		return query


if __name__ == '__main__':
	urlparse = Urlparse()
	print urlparse.parse_query('http://www.cwi.nl:80/%7Eguido/Python.com;a=123&b=12?name=xyz&name1=abc&relationship=friends')
