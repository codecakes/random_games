#A simple counting sort - probablythe cleanest solution I ever wrote!
#Does not take into account stability and order.
#No array checking yet for integer type.
#Assuming incoming array is strictly an integer array/list

def store(alist):
    """increment counter in a counter array for every integer encountered"""
    klist = [0] * (max(alist)+1)  #O(n)
    #O(n)
    for i in alist:
        klist[i] += 1
    return klist

def execute(klist):
    """create a list and extend every encountered indexin a list by the count"""
    output = []
    for l in xrange(len(klist)):
        if klist[l]:
            output += [l]*klist[l]
    return output

def execute_clr(alist, klist):
    """you dont wana know. inplace klist manipulation. creates new sorted list."""
    output = [0] * len(alist)
    sm = 0
    
    #update klist according to the wierd logic
    for index in xrange(len(klist)):
        klist[index] += sm
        sm = klist[index]
    
    for index in xrange(len(alist)-1, -1, -1):
        a_index = alist[index]
        klist[a_index] -=  1
        kval = klist[a_index]
        output[kval] = a_index
    return output

def count_int_sort(alist):
    """Sort an integer array using counting sort"""
    return execute(store(alist))  #O(len(klist))

def count_int_clr_sort(alist):
    """Sort an integer array using weird counting sort logic"""
    return execute_clr(alist, store(alist))

