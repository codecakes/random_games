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
"""

def cmp_sort(l1, l2, alist, index, grand_iter):
    iter_count = 0
    second_while = 0
    #given two sorted arrays
    i = j = inc = incmax = 0
    #print "the list {}\n".format(alist)
    smaller,larger = (l1,l2) if(len(l1)<len(l2)) else (l2,l1)
    #print "left {} right {}\n".format(smaller, larger)
    imax = len(smaller)
    jmax = len(larger)

    while (i < imax) and (j < jmax):
        iter_count += 1
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
        second_while += 1
        alist[index] = l[inc]
        inc += 1
        index += 1

    #print "list: {}".format(alist)
    grand_iter[0] += max((second_while, iter_count))
    print grand_iter
    return alist

def merge_sort_rec(alist, grand_iter = [0], index = 0):
    ln = len(alist)
    mid = ln//2
    grand_iter[0] += 1
    #print "index is {}".format(index)
    #break down until base case of len =1 remains
    if mid >= 1:
        #print "Splitting...{}\n".format(alist)
        left = merge_sort_rec(alist[:mid], grand_iter = grand_iter)[0]
        right = merge_sort_rec(alist[mid:], grand_iter = grand_iter)[0]
        #print "left {}\n".format(left)
        #print "right {}\n".format(right)
        return cmp_sort(left, right, alist, index, grand_iter), grand_iter
    else:
        return alist, grand_iter


if __name__ == "__main__":
    tmp = []
    for _ in xrange(20):
        l = [randint(1,100) for _ in xrange(randint(1,20))]
        ln = len(l)
        grand_iter = [0]
        counts = merge_sort_rec(l, grand_iter=grand_iter)[1]
        tmp.append((ln, counts, ln*log(ln, 2)))

    tmp_arr = np.array(map(sorted, np.array(tmp).transpose()))
    plot(tmp_arr[0], tmp_arr[1])
    plot(tmp_arr[0], tmp_arr[2])
