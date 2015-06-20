
from collections import Counter

def counting(arr):
    '''creating an indexed counting array using Optimal Counter module'''
    count = Counter(arr)
    return [count.get(i, 0) for i in xrange(max(count.viewkeys()))]
