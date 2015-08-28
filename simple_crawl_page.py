# Simple page link crawler using PageRank. for academic purpose only.

import re
from string import punctuation
import requests

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
            '<p> It is a good idea to '
            '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
            'crawl</a> before you try to  '
            '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
            'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
            '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
        elif url == "http://top.contributors/velak.html":
            return ('<a href="http://top.contributors/jesyspa.html">'
        '<a href="http://top.contributors/forbiddenvoid.html">')
        elif url == "http://top.contributors/jesyspa.html":
            return  ('<a href="http://top.contributors/elssar.html">'
        '<a href="http://top.contributors/kilaws.html">')
        elif url == "http://top.contributors/forbiddenvoid.html":
            return ('<a href="http://top.contributors/charlzz.html">'
        '<a href="http://top.contributors/johang.html">'
        '<a href="http://top.contributors/graemeblake.html">')
        elif url == "http://top.contributors/kilaws.html":
            return ('<a href="http://top.contributors/tomvandenbosch.html">'
        '<a href="http://top.contributors/mathprof.html">')
        elif url == "http://top.contributors/graemeblake.html":
            return ('<a href="http://top.contributors/dreyescat.html">'
        '<a href="http://top.contributors/angel.html">')
        elif url == "A1":
            return  '<a href="B1"> <a href="C1">  '
        elif url == "B1":
            return  '<a href="E1">'
        elif url == "C1":
            return '<a href="D1">'
        elif url == "D1":
            return '<a href="E1"> '
        elif url == "E1":
            return '<a href="F1"> '
        else:
            return requests.get(url).content
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

"""
def crawl_web(seed,max_depth):
    crawled = []
    level = 0
    if max_depth == 0:
        return [seed]
    dct = {level:[seed]}
    #breadth first then depth level compare
    while level <= max_depth:
        #print "level is %s dct is %s" %(level, dct)
        if dct[level] == []:
            level += 1
        #if list empty at that level in dict
        if level not in dct or dct[level] == []: break
        #print "popping from {} at level {}".format(dct[level], level)
        page = dct[level].pop()
        if page not in crawled:
            #print "page is %s at depth %s" %(page,level)
            tmp = [each_link for each_link in get_all_links(get_page(page))]
            if tmp:
                if level+1 in dct:
                    dct[level+1].extend(tmp)
                else:
                    dct[level+1] = tmp
            #union(tocrawl, tmp)
            if level <= max_depth:
                crawled.append(page)
    #print "=="*10
    return crawled
"""

def lookup(index, keyword):
    return index.get(keyword, None)

def add_keyword_to_index(index, keyword, url):
    index.setdefault(keyword, []).append(url)
    #if keyword in index:
    #    index[keyword].append(url)
    #for each in index:
    #    if each[0] == keyword:
    #        if url not in each[1]:
    #            each[1].append(url)
    #            return
    #else:
    #    #index.append([keyword, [url]])
    #    index[keyword] = [url]


def split_string(source,splitlist):
    pat = '|'.join(["[\{}]+".format(e) for e in list(splitlist)]) \
            if "," != splitlist else ","
    return reduce(lambda x,y: x+y, \
           [w.split() for w in re.split(pat, source) if w]) \
           if "," != splitlist else \
           [w.strip() for w in re.split(pat, source) if w]

def add_urls_to_index(index, page_url, content):
    #content = [w.strip() for w in content.split()]
    content = split_string(content, punctuation) if content else ''
    [add_keyword_to_index(index, each_wrd, page_url) \
    for each_wrd in content if each_wrd]
        
    return

def crawl_web(seed,max_depth):
    '''A more elegant design'''
    tocrawl = [seed]
    crawled = []
    next_depth = []
    #index = []
    index = {}
    graph = {}
    depth = 0
    #if you want depth specify
    while tocrawl and depth <= max_depth:
        page_url = tocrawl.pop()
        if page_url not in crawled:
            #get the html content from page url
            content = get_page(page_url)
            #get all parsable links from the html content
            all_links = get_all_links(content)
            #this is what adds urls to a keyword in index
            add_urls_to_index(index, page_url, content)
            #map the current page url to all links it outlinks to
            graph.setdefault(page_url, []).extend(all_links)
            #append all new links to parse
            union(next_depth, all_links)
            crawled.append(page_url)
        #once tocrawl is empty=the breadth of that level is empty
        #move to crawling next level of links
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth = depth + 1
    return crawled

assert sorted(crawl_web("http://www.udacity.com/cs101x/index.html",0)) == \
sorted(['http://www.udacity.com/cs101x/index.html'])

assert sorted(crawl_web("http://www.udacity.com/cs101x/index.html",1)) == \
sorted(['http://www.udacity.com/cs101x/index.html',
'http://www.udacity.com/cs101x/flying.html',
'http://www.udacity.com/cs101x/walking.html',
'http://www.udacity.com/cs101x/crawling.html'])

assert sorted(crawl_web("http://www.udacity.com/cs101x/index.html",50)) == \
sorted(['http://www.udacity.com/cs101x/index.html',
'http://www.udacity.com/cs101x/flying.html',
'http://www.udacity.com/cs101x/walking.html',
'http://www.udacity.com/cs101x/crawling.html',
'http://www.udacity.com/cs101x/kicking.html'])

assert sorted(crawl_web("http://top.contributors/forbiddenvoid.html",2)) == \
sorted(['http://top.contributors/forbiddenvoid.html',
'http://top.contributors/graemeblake.html',
'http://top.contributors/angel.html',
'http://top.contributors/dreyescat.html',
'http://top.contributors/johang.html',
'http://top.contributors/charlzz.html'])

assert sorted(crawl_web("A1",3)) == \
sorted(['A1', 'C1', 'B1', 'E1', 'D1', 'F1'])
# (May be in any order)

assert sorted(crawl_web("A1",2)) == \
sorted(['A1', 'B1', 'C1', 'D1', 'E1'])

def dance(seed,max_depth):
    '''A more elegant design'''
    tocrawl = [seed]
    crawled = []
    next_depth = []
    index = {}
    graph = {}
    depth = 0
    #if you want depth specify
    while tocrawl and depth <= max_depth:
        page_url = tocrawl.pop()
        if page_url not in crawled:
            #get the html content from page url
            content = get_page(page_url)
            #get all parsable links from the html content
            all_links = get_all_links(content)
            #this is what adds urls to a keyword in index
            add_urls_to_index(index, page_url, content)
            #map the current page url to all links it outlinks to
            graph.setdefault(page_url, []).extend(all_links)
            #append all new links to parse
            union(next_depth, all_links)
            crawled.append(page_url)
        #once tocrawl is empty=the breadth of that level is empty
        #move to crawling next level of links
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth = depth + 1
    return index, graph



#Finishing the page ranking algorithm.
def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    npages_r = 1.0 / npages
    initial_damping = (1 - d) / npages
    
    for page in graph:
        ranks[page] = npages_r
    
    #TODO: Transform inner loop into NP Matrix
    #TODO: Transform outer loop markov Chained matrices
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            inlinks = [each_url for each_url in graph if page in graph[each_url]]
            #page rank logic
            #each time iteration, the url rank changes based on previous.
            #More the inlinks to a url, lesser its value.
            newrank = initial_damping + (d * sum([ranks[each_url]/float(len(graph[each_url])) \
                                for each_url in inlinks]))
            
            newranks[page] = newrank
        ranks = newranks
    return ranks