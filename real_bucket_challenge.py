#Given two Jugs small and large

#While large != X Ltrs
#Fill small Full
#Pour small -> large 
#if large Full -> Empty
#if small not Empty: pour small -> large
#Fill small Full
#Pour small -> large till Full

"""Inspiration:
MIT 6.042j: Explores the basics of number theory
and algorithms for computation with integers.
Motivation to: GCD ;-)
"""

from collections import deque

def fill(container):
    if len(container) < container.maxlen:
        diff = container.maxlen - len(container)
        [container.append(1) for _ in xrange(diff)]
        print "after filling container %s" %(container)

def pour(cn1, cn2):
    if len(cn1) and (len(cn2) < cn2.maxlen) and cn1.maxlen < cn2.maxlen:
        diff = cn2.maxlen - len(cn2)
        [cn2.append(cn1.pop()) for _ in xrange(diff) if cn1]
        print "after pouring %s and %s" %(cn1, cn2)

def empty(container):
    container.clear()
    print "container clear"
    
def fill_buck(small, large, target_val):
    large_val = large.maxlen
    print "target val %s large val %s" %(target_val, large_val)
    if target_val < large_val:
        while len(large)!= target_val:
            print "target val %s large %s" %(target_val, large)
            fill(small)
            pour(small, large)
            #if len(large) == large_val:
            #    empty(large)
            if len(small):
                #if small not empty?
                if len(large) == large_val:
                    empty(large)
                pour(small, large)

def run_bucks(small_max, large_max, target_val):
    small = deque(maxlen=small_max)
    large = deque(maxlen=large_max)
    fill_buck(small, large, target_val)

if __name__ == "__main__":
    run_bucks(3, 5, 4)
    run_bucks(4, 6, 2)
    run_bucks(44, 55, 11)