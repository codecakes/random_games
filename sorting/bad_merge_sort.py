"""
How to implement a BAD merge sort
"""

from math import log, ceil
from numpy import randint
from matplotlib.pyplot import plot

def swap_cmp(num1, num2):
    return [num1,num2] if num1 < num2 else [num2, num1]

def cmp_sort(l1, l2):
    #given two sorted arrays
    i = j = 0
    tmp_list = []
    smaller,larger = (l1,l2) if(len(l1)<len(l2)) else (l2,l1)
    #print smaller, larger
    imax = len(smaller)
    jmax = len(larger)
    #print imax,jmax

    while (i < imax) and (j < jmax):
        if smaller[i] > larger[j]:
            tmp_list.append(larger[j])
            j += 1
        else:
            tmp_list.append(smaller[i])
            i += 1
        #print tmp_list
        #print "index i {} j {}".format(i,j)

    return tmp_list + smaller[i:] if jmax - j < imax - i else tmp_list + larger[j:]

def merge_sort(unsorted_list):
    # A quadratic solution to an nlogn problem
    types = (int, float)
    grand_count = it_count = 0

    if len(unsorted_list) < 2:
        return unsorted_list, grand_count*it_count
    l = unsorted_list
    ln = len(l)
    levels = int(ceil(log(ln, 2)))

    for _ in xrange(levels):
        grand_count += 1
        tmp_list = []
        #print "length ln is {}".format(ln)
        for index in xrange(0, ln, 2):
            it_count += 1
            #print "iterations index is {}".format(index)
            l1 = l[index]
            if index+1 < ln:
                l2 = l[index+1]
                if isinstance(l1, list) and isinstance(l2, list):
                    res = cmp_sort(l1,l2)
                elif isinstance(l1, types) and isinstance(l2, types):
                    res = swap_cmp(l1, l2)
                tmp_list.append(res)
            elif isinstance(l1, list):
                tmp_list.append(l1)
            elif isinstance(l1, types):
                tmp_list.append([l1])
        l = tmp_list
        ln = len(l)
        #print "after merge iteration: {}".format(l)
    #del tmp_list, res, l1, l2, ln, levels
    return l[0], grand_count*it_count

if __name__ == "__main__":

    tmp = []
    for _ in xrange(20):
        l=[randint(1,100) for _ in xrange(randint(1,20))]
        ln = len(l)
        res = merge_sort(l)
        #cmp nlogn VS. actual levels * counts time.
        tmp.append((ln, ln*log(ln,2), res[1]))
    print tmp
    tmp_arr = np.array(tmp).transpose()
    #cmp with nlogn
    plot(map(sorted, (tmp_arr[0], tmp_arr[1])))
    #cmp with the above solution iterations
    plot(map(sorted, (tmp_arr[0], tmp_arr[2])))
