def cmp_sort(l1, l2, alist, index):
    #given two sorted arrays
    i = j = inc = incmax = 0
    #tmp_list = []
    smaller,larger = (l1,l2) if(len(l1)<len(l2)) else (l2,l1)
    #print smaller, larger
    imax = len(smaller)
    jmax = len(larger)
    #print imax,jmax

    while (i < imax) and (j < jmax):
        if smaller[i] > larger[j]:
            #tmp_list.append(larger[j])
            alist[index] = larger[j]
            j += 1
            index += 1
        else:
            #tmp_list.append(smaller[i])
            alist[index] = smaller[i]
            i += 1
            index += 1
        #print tmp_list
        #print "index i {} j {}".format(i,j)

    if jmax - j < imax - i:
        inc = i
        incmax = imax
        l = smaller
    else:
        inc = j
        incmax = jmax
        l = larger

    while incmax-inc != 0:
        alist[index] = l[inc]
        inc += 1
        index += 1

    #return tmp_list + smaller[i:]  else tmp_list + larger[j:]
    return alist

def merge_sort_rec(alist, index = 0):
    ln = len(alist)
    mid = ln//2
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
