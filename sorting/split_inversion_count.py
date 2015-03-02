"""
To understand what's going on:
1. The Merge Sort Recursively breaks down a list of size N to
left and right, each of size N/2;
2. The new sliced lists are fed to cmp_sort that rearranges the
fed total list of size N with index to be sorted in the original list.
Since, Original list is Mutable - This Original list can be
either Sliced list or Original List.
3. Each time if the right half element in comparing is less than left half,
increment a 1 to the split_conversion to show that the right element is less in order than the left one;
4. Until sliced lists are merged recursively back to Parent List.

Turn on the comments to see what's happening.
"""

def cmp_sort(l1, l2, alist, index, split_conv):
    #given two sorted arrays
    i = j = inc = incmax = 0
    #print "the list {}\n".format(alist)
    smaller,larger = (l1,l2) #if(len(l1)<len(l2)) else (l2,l1)
    #print "left {} right {}\n".format(smaller, larger)
    imax = len(smaller)
    jmax = len(larger)

    while (i < imax) and (j < jmax):
        if smaller[i] > larger[j]:
            alist[index] = larger[j]
            j += 1
            index += 1
            split_conv[0] += imax - i
        else:
            #smaller[i] <= larger[j]:
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

def split_inv_merge_sort(alist, split_conv = [0], index = 0):
    ln = len(alist)
    mid = ln//2
    #print "index is {}".format(index)
    #break down until base case of len =1 remains
    if mid >= 1:
        #print "Splitting...{}\n".format(alist)
        left = split_inv_merge_sort(alist[:mid], split_conv=split_conv)
        left = left[0] if isinstance(left[0], list) else left
        right = split_inv_merge_sort(alist[mid:], split_conv=split_conv)
        right = right[0] if isinstance(right[0], list) else right
        #print "left {}\n".format(left)
        #print "right {}\n".format(right)
        return cmp_sort(left, right, alist, index, split_conv), split_conv
    else:
        return alist