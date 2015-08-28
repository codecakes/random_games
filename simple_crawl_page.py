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
    exists = index.get(keyword, None)
    if exists:
        if url not in exists:
            index.setdefault(keyword, []).append(url)
    else:
        index.setdefault(keyword, []).append(url)

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
    #print graph
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
    '''A more elegant design
    index: {keyword: [list of urls]}
    '''
    tocrawl = [seed]
    crawled = []
    next_depth = []
    index = {}
    graph = {}
    depth = 0
    #if you want depth specify
    while tocrawl:
        if not depth <= max_depth and max_depth != -1: break
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

def crawl_web2(seed):
    '''A more elegant design'''
    tocrawl = [seed]
    crawled = []
    next_depth = []
    #index = []
    index = {}
    graph = {}
    depth = 0
    #if you want depth specify
    while tocrawl:
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
    #print graph
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

#I'm feeling lucky
def lucky_search(index, ranks, keyword):
    if keyword not in index: return None
    return max([(url, ranks[url]) for url in index[keyword]], \
                key = lambda x: x[1])[0]

#ordered result form high to low rank
def ordered_search(index, ranks, keyword):
    #print index.get(keyword, None)
    return [url[0] for url in \
        sorted([(each_url, ranks[each_url]) \
                for each_url in index[keyword]], \
                key=lambda r: r[1], reverse=True)] if keyword in index \
                                                    else None

if __name__ == "__main__":
        
    ##Tests
    
    #setup
    cache = {
    'http://udacity.com/cs101x/urank/index.html': """<html>
    <body>
    <h1>Dave's Cooking Algorithms</h1>
    <p>
    Here are my favorite recipies:
    <ul>
    <li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
    <li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
    <li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
    </ul>
    
    For more expert opinions, check out the 
    <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
    and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
    </body>
    </html>
    
    
    
    
    
    
    """,
    'http://udacity.com/cs101x/urank/zinc.html': """<html>
    <body>
    <h1>The Zinc Chef</h1>
    <p>
    I learned everything I know from 
    <a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
    </p>
    <p>
    For great hummus, try 
    <a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.
    
    </body>
    </html>
    
    
    
    
    
    
    """,
    'http://udacity.com/cs101x/urank/nickel.html': """<html>
    <body>
    <h1>The Nickel Chef</h1>
    <p>
    This is the
    <a href="http://udacity.com/cs101x/urank/kathleen.html">
    best Hummus recipe!
    </a>
    
    </body>
    </html>
    
    
    
    
    
    
    """,
    'http://udacity.com/cs101x/urank/kathleen.html': """<html>
    <body>
    <h1>
    Kathleen's Hummus Recipe
    </h1>
    <p>
    
    <ol>
    <li> Open a can of garbonzo beans.
    <li> Crush them in a blender.
    <li> Add 3 tablesppons of tahini sauce.
    <li> Squeeze in one lemon.
    <li> Add salt, pepper, and buttercream frosting to taste.
    </ol>
    
    </body>
    </html>
    
    """,
    'http://udacity.com/cs101x/urank/arsenic.html': """<html>
    <body>
    <h1>
    The Arsenic Chef's World Famous Hummus Recipe
    </h1>
    <p>
    
    <ol>
    <li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
    <li> Force her to make hummus for you.
    </ol>
    
    </body>
    </html>
    
    """,
    'http://udacity.com/cs101x/urank/hummus.html': """<html>
    <body>
    <h1>
    Hummus Recipe
    </h1>
    <p>
    
    <ol>
    <li> Go to the store and buy a container of hummus.
    <li> Open it.
    </ol>
    
    </body>
    </html>
    
    
    
    
    """,
    }
    
    def get_page(url):
        try:
            if url in cache:
                return cache[url]
            else:
                return requests.get(url).content
        except Exception as e:
            print e
            return "" 
    
    
    index, graph = dance('http://udacity.com/cs101x/urank/index.html', -1)
    #print graph
    ranks = compute_ranks(graph)
    
    assert lucky_search(index, ranks, 'Hummus')== \
    "http://udacity.com/cs101x/urank/kathleen.html"
    
    assert lucky_search(index, ranks, 'the') == \
    "http://udacity.com/cs101x/urank/nickel.html"
    
    assert lucky_search(index, ranks, 'babaganoush') == \
    None
    

    cache = {
    'http://udacity.com/cs101x/urank/index.html': """<html>
    <body>
    <h1>Dave's Cooking Algorithms</h1>
    <p>
    Here are my favorite recipies:
    <ul>
    <li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
    <li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
    <li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
    </ul>
    
    For more expert opinions, check out the
    <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>
    and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
    </body>
    </html>
    
    
    
    
    
    
    """,
    'http://udacity.com/cs101x/urank/zinc.html': """<html>
    <body>
    <h1>The Zinc Chef</h1>
    <p>
    I learned everything I know from
    <a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
    </p>
    <p>
    For great hummus, try
    <a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.
    
    </body>
    </html>
    
    
    
    
    
    
    """,
    'http://udacity.com/cs101x/urank/nickel.html': """<html>
    <body>
    <h1>The Nickel Chef</h1>
    <p>
    This is the
    <a href="http://udacity.com/cs101x/urank/kathleen.html">
    best Hummus recipe!
    </a>
    
    </body>
    </html>
    
    
    
    
    
    
    """,
    'http://udacity.com/cs101x/urank/kathleen.html': """<html>
    <body>
    <h1>
    Kathleen's Hummus Recipe
    </h1>
    <p>
    
    <ol>
    <li> Open a can of garbonzo beans.
    <li> Crush them in a blender.
    <li> Add 3 tablesppons of tahini sauce.
    <li> Squeeze in one lemon.
    <li> Add salt, pepper, and buttercream frosting to taste.
    </ol>
    
    </body>
    </html>
    
    """,
    'http://udacity.com/cs101x/urank/arsenic.html': """<html>
    <body>
    <h1>
    The Arsenic Chef's World Famous Hummus Recipe
    </h1>
    <p>
    
    <ol>
    <li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
    <li> Force her to make hummus for you.
    </ol>
    
    </body>
    </html>
    
    """,
    'http://udacity.com/cs101x/urank/hummus.html': """<html>
    <body>
    <h1>
    Hummus Recipe
    </h1>
    <p>
    
    <ol>
    <li> Go to the store and buy a container of hummus.
    <li> Open it.
    </ol>
    
    </body>
    </html>
    
    
    
    
    """,
    }
    
    index, graph = dance('http://udacity.com/cs101x/urank/index.html', -1)
    ranks = compute_ranks(graph)
    
    assert ordered_search(index, ranks, 'Hummus') == \
    ['http://udacity.com/cs101x/urank/kathleen.html',
        'http://udacity.com/cs101x/urank/nickel.html',
        'http://udacity.com/cs101x/urank/arsenic.html',
        'http://udacity.com/cs101x/urank/hummus.html',
        'http://udacity.com/cs101x/urank/index.html']
    
    assert ordered_search(index, ranks, 'babaganoush') == None
    
    
    