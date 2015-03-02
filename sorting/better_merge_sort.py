"""
To understand what's going on:
1. The Merge Sort Recursively breaks down a list of size N to
left and right, each of size N/2;
2. The new sliced lists are fed to cmp_sort that rearranges the
fed total list of size N with index to be sorted in the original list.
Since, Original list is Mutable - This Original list can be
either Sliced list or Original List.
3. Until sliced lists are merged recursively back to Parent List.

Turn on the comments to see what's happening.

Order for sanity check is based on Master Method:
    T(n) <= aT(n/b) + O(n^d)
    Tn = O(n^dlogn) | a = b^d
    Tn = O(n^d) | a<b^d
    Tn = O(n^logd, base=b) | a > b^d
"""

def cmp_sort(l1, l2, alist, index):
    #given two sorted arrays
    i = j = inc = incmax = 0
    #print "the list {}\n".format(alist)
    smaller,larger = (l1,l2) if(len(l1)<=len(l2)) else (l2,l1)
    #print "left {} right {}\n".format(smaller, larger)
    imax = len(smaller)
    jmax = len(larger)

    while (i < imax) and (j < jmax):
        if smaller[i] > larger[j]:
            alist[index] = larger[j]
            j += 1
            index += 1
        else:
            alist[index] = smaller[i]
            i += 1
            index += 1
        #print "index i {} j {} index {}".format(i,j, index)
    if jmax - j < imax - i:
        inc = i
        incmax = imax
        l = smaller
    else:
        inc = j
        incmax = jmax
        l = larger

    while incmax != inc:
        alist[index] = l[inc]
        inc += 1
        index += 1
    #print "list: {}".format(alist)
    return alist

def merge_sort_rec(alist, index = 0):
    ln = len(alist)
    mid = ln//2
    #print "index is {}".format(index)
    #break down until base case of len =1 remains
    if mid >= 1:
        #print "Splitting...{}\n".format(alist)
        left = merge_sort_rec(alist[:mid])
        right = merge_sort_rec(alist[mid:])
        #print "left {}\n".format(left)
        #print "right {}\n".format(right)
        return cmp_sort(left, right, alist, index)
    else:
        return alist
