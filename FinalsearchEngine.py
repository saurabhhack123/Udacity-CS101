#Finishing the search engine python program by saurabh saxena(copyright 2012)
#Motivation stanford lectures and research paper by Larry Page and Sergey Bin 
import urllib

def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""

crawl_depth = 1

split_list = " ,!-<>"

def dfs(graph, node, visited):
    if node in visited:
         return []
    visited.append(node)
    for neighbor in graph[node]:
         for visit in dfs(graph, neighbor, visited):
              if visit not in visited:
                  visited.append(visit)
    return visited
    



def reachable(graph, node):
     return dfs(graph, node, [])
	 

	 
def edit_distance(s,t):
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)
    if s[0] == t[0]:
        return edit_distance(s[1:], t[1:])
    else:
        return min( 1 + edit_distance(s[1:], t[1:]),
                     1 + edit_distance(s, t[1:]),
                     1 + edit_distance(s[1:], t))

def multi_lookup(index, keywords):
            if not keywords:
                  return [ ]
            activepos = lookup(index, keywords[0])
            for keyword in keywords[1:]:
                newactivepos = [ ]
                nexturlpos = lookup(index, keyword)
                if nexturlpos:
                    for pos in activepos:
                        if [pos[0], pos[1] + 1] in nexturlpos:
                             newactivepos.append([pos[0], pos[1] + 1])
                activepos = newactivepos
            result = []
            for pos in activepos:
                 result.append(pos[0])
            return result
         

def split_string(source, splitlist = split_list):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        elif atsplit:
            output.append(char)
            atsplit = False
        else:
            output[-1] += char
    return output

def lucky_search(index, ranks, keyword):
     pages = lookup(index, keyword)
     if not pages:
        return None
     best_page = pages[0]
     for candidate in pages:
        if ranks[candidate] > ranks[best_page]:
             best_page = candidate
     return best_page
			 
def quicksort_pages(pages, ranks):
    if not pages or len(pages) <= 1:
         return pages
    else:
        pivot = ranks[pages[0]]
        worse = []
        better = []
        for page in pages[1:]:
            if ranks[page] <= pivot:
                worse.append(page)
            else:
                better.append(page)
        return quicksort_pages(better, ranks) + [pages[0]]

def ordered_search(index, ranks, keyword):
           pages = lookup(index, keyword)
           return quicksort_pages(pages, ranks)
		   
def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            
            newranks[page] = newrank
        ranks = newranks
    return ranks
	
def crawl_web(seed, max_depth = crawl_depth): 
    tocrawl = [[seed, 0]]
    crawled = []
    graph = {}  
    index = {} 
    while tocrawl: 
        page, depth = tocrawl.pop()
        if page not in crawled and depth <= max_depth:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content) 
            graph[page] = outlinks
            for link in outlinks:
                tocrawl.append([link, depth + 1])
            crawled.append(page)
    return index, graph
    
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links
	
def add_page_to_index(index, url, content):
    words = split_string(content)
	position = 0
    for word in words:
        add_to_index(index, word, url, position)
		position = position + 1
        
def add_to_index(index, keyword, url, position):
    if keyword in index:
        index[keyword].append([url, position])
    else:
        index[keyword] = [[url, position]]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

index, graph = crawl_web('http://')

ranks = compute_ranks(graph)
