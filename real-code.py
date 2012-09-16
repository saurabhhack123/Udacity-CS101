Python 2.7.2 (default, Jun 12 2011, 15:08:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> def get_page(url):
	try:
	     return urllib.urlopen(url).read()
	except:
             return ""

        
>>> def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = pade.find('"', start_quot + 1)
	url = page[start_quote + 1:end_quote]
	return url, end_quote

>>> def get_all_links(page):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
		     links.append(url)
		     page = page[endpos:]
		else:
		      break
	return links

>>> def union(a, b):
	for e in b:
	     if e not in a:
		     a.append(e)

>>> def add_page_to_index(index, url, content):
	words = content.split()
	for word in words:
		add_to_index(index, word, url)

>>> def add_to_index(index, keyword, url):
	if keyword in index:
		index[keyword].append(url)
	else:
		index[keyword] = [url]

>>> def lookup(index, keyword):
	if keyword in index:
		return index[keyword]
	else:
		return None

>>> def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	graph = {}
	index = {}
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index, page, content)
			outlinks = get_all_links(content)
			graph[page] = outlinks
			union(tocrawl, outlinks)
			crawled.append(page)
	return index, graph

>>> index,graph = crawl_web('http://www.udacity.com/cs101x/final/multi.html')
>>> 
>>> print lookup(index,"good")
None
>>> print lookup(index,"<html>")
None
>>> if 'http://udacity.com/cs101x/urank/index.html' in graph:
    print graph['http://udacity.com/cs101x/urank/index.html']

>>> print index["good"]

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print index["good"]
KeyError: 'good'
>>> print index
{'server.</h2>': ['http://www.udacity.com/cs101x/final/multi.html'], 'text=#000000': ['http://www.udacity.com/cs101x/final/multi.html'], '<h2>The': ['http://www.udacity.com/cs101x/final/multi.html'], 'bgcolor=#ffffff>': ['http://www.udacity.com/cs101x/final/multi.html'], '<h2></h2>': ['http://www.udacity.com/cs101x/final/multi.html'], '<body': ['http://www.udacity.com/cs101x/final/multi.html'], '<html><head>': ['http://www.udacity.com/cs101x/final/multi.html'], '<meta': ['http://www.udacity.com/cs101x/final/multi.html'], 'http-equiv="content-type"': ['http://www.udacity.com/cs101x/final/multi.html'], 'Not': ['http://www.udacity.com/cs101x/final/multi.html', 'http://www.udacity.com/cs101x/final/multi.html'], 'Found</title>': ['http://www.udacity.com/cs101x/final/multi.html'], '<code>/cs101x/final/multi.html</code>': ['http://www.udacity.com/cs101x/final/multi.html'], 'was': ['http://www.udacity.com/cs101x/final/multi.html'], 'content="text/html;charset=utf-8">': ['http://www.udacity.com/cs101x/final/multi.html'], '<title>404': ['http://www.udacity.com/cs101x/final/multi.html'], 'requested': ['http://www.udacity.com/cs101x/final/multi.html'], '</body></html>': ['http://www.udacity.com/cs101x/final/multi.html'], 'URL': ['http://www.udacity.com/cs101x/final/multi.html'], 'Found</h1>': ['http://www.udacity.com/cs101x/final/multi.html'], 'not': ['http://www.udacity.com/cs101x/final/multi.html'], 'on': ['http://www.udacity.com/cs101x/final/multi.html'], 'this': ['http://www.udacity.com/cs101x/final/multi.html'], '<h1>Error:': ['http://www.udacity.com/cs101x/final/multi.html'], '</head>': ['http://www.udacity.com/cs101x/final/multi.html'], 'found': ['http://www.udacity.com/cs101x/final/multi.html']}
>>> print lookup(index,"requested")
['http://www.udacity.com/cs101x/final/multi.html']
>>> print lookup(index,"<h1>Error:")
['http://www.udacity.com/cs101x/final/multi.html']
>>> index,graph = crawl_web('http://www.vit.ac.in/informationfor/Parents.asp')

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    index,graph = crawl_web('http://www.vit.ac.in/informationfor/Parents.asp')
  File "<pyshell#65>", line 11, in crawl_web
    outlinks = get_all_links(content)
  File "<pyshell#26>", line 4, in get_all_links
    url, endpos = get_next_target(page)
  File "<pyshell#15>", line 6, in get_next_target
    end_quote = pade.find('"', start_quot + 1)
NameError: global name 'pade' is not defined

>>> print index
{'server.</h2>': ['http://www.udacity.com/cs101x/final/multi.html'], 'text=#000000': ['http://www.udacity.com/cs101x/final/multi.html'], '<h2>The': ['http://www.udacity.com/cs101x/final/multi.html'], 'bgcolor=#ffffff>': ['http://www.udacity.com/cs101x/final/multi.html'], '<h2></h2>': ['http://www.udacity.com/cs101x/final/multi.html'], '<body': ['http://www.udacity.com/cs101x/final/multi.html'], '<html><head>': ['http://www.udacity.com/cs101x/final/multi.html'], '<meta': ['http://www.udacity.com/cs101x/final/multi.html'], 'http-equiv="content-type"': ['http://www.udacity.com/cs101x/final/multi.html'], 'Not': ['http://www.udacity.com/cs101x/final/multi.html', 'http://www.udacity.com/cs101x/final/multi.html'], 'Found</title>': ['http://www.udacity.com/cs101x/final/multi.html'], '<code>/cs101x/final/multi.html</code>': ['http://www.udacity.com/cs101x/final/multi.html'], 'was': ['http://www.udacity.com/cs101x/final/multi.html'], 'content="text/html;charset=utf-8">': ['http://www.udacity.com/cs101x/final/multi.html'], '<title>404': ['http://www.udacity.com/cs101x/final/multi.html'], 'requested': ['http://www.udacity.com/cs101x/final/multi.html'], '</body></html>': ['http://www.udacity.com/cs101x/final/multi.html'], 'URL': ['http://www.udacity.com/cs101x/final/multi.html'], 'Found</h1>': ['http://www.udacity.com/cs101x/final/multi.html'], 'not': ['http://www.udacity.com/cs101x/final/multi.html'], 'on': ['http://www.udacity.com/cs101x/final/multi.html'], 'this': ['http://www.udacity.com/cs101x/final/multi.html'], '<h1>Error:': ['http://www.udacity.com/cs101x/final/multi.html'], '</head>': ['http://www.udacity.com/cs101x/final/multi.html'], 'found': ['http://www.udacity.com/cs101x/final/multi.html']}
>>> 
KeyboardInterrupt
>>> def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quot + 1)
	url = page[start_quote + 1:end_quote]
	return url, end_quote

>>> print index
{'server.</h2>': ['http://www.udacity.com/cs101x/final/multi.html'], 'text=#000000': ['http://www.udacity.com/cs101x/final/multi.html'], '<h2>The': ['http://www.udacity.com/cs101x/final/multi.html'], 'bgcolor=#ffffff>': ['http://www.udacity.com/cs101x/final/multi.html'], '<h2></h2>': ['http://www.udacity.com/cs101x/final/multi.html'], '<body': ['http://www.udacity.com/cs101x/final/multi.html'], '<html><head>': ['http://www.udacity.com/cs101x/final/multi.html'], '<meta': ['http://www.udacity.com/cs101x/final/multi.html'], 'http-equiv="content-type"': ['http://www.udacity.com/cs101x/final/multi.html'], 'Not': ['http://www.udacity.com/cs101x/final/multi.html', 'http://www.udacity.com/cs101x/final/multi.html'], 'Found</title>': ['http://www.udacity.com/cs101x/final/multi.html'], '<code>/cs101x/final/multi.html</code>': ['http://www.udacity.com/cs101x/final/multi.html'], 'was': ['http://www.udacity.com/cs101x/final/multi.html'], 'content="text/html;charset=utf-8">': ['http://www.udacity.com/cs101x/final/multi.html'], '<title>404': ['http://www.udacity.com/cs101x/final/multi.html'], 'requested': ['http://www.udacity.com/cs101x/final/multi.html'], '</body></html>': ['http://www.udacity.com/cs101x/final/multi.html'], 'URL': ['http://www.udacity.com/cs101x/final/multi.html'], 'Found</h1>': ['http://www.udacity.com/cs101x/final/multi.html'], 'not': ['http://www.udacity.com/cs101x/final/multi.html'], 'on': ['http://www.udacity.com/cs101x/final/multi.html'], 'this': ['http://www.udacity.com/cs101x/final/multi.html'], '<h1>Error:': ['http://www.udacity.com/cs101x/final/multi.html'], '</head>': ['http://www.udacity.com/cs101x/final/multi.html'], 'found': ['http://www.udacity.com/cs101x/final/multi.html']}
>>> index,graph = crawl_web('http://www.vit.ac.in/informationfor/Parents.asp')

Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    index,graph = crawl_web('http://www.vit.ac.in/informationfor/Parents.asp')
  File "<pyshell#65>", line 11, in crawl_web
    outlinks = get_all_links(content)
  File "<pyshell#26>", line 4, in get_all_links
    url, endpos = get_next_target(page)
  File "<pyshell#79>", line 6, in get_next_target
    end_quote = page.find('"', start_quot + 1)
NameError: global name 'start_quot' is not defined
>>> def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1:end_quote]
	return url, end_quote

>>> index,graph = crawl_web('http://www.vit.ac.in/informationfor/Parents.asp')








 
             
