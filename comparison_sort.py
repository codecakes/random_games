#comparison sort - probablythe cleanest solution I ever wrote!
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

def cmp_int_sort(alist):
    """Sort an integer array using comparison sort"""
    return execute(store(alist))  #O(len(klist))