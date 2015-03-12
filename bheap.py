#!/usr/bin/python

"""
Create a heapq python implementation.
this works:
    import heapq
    alist = [21, 44, 37, 38, 24, 2, 10, 44]
    heapq.heapify(alist)
    print alist
    alist = [21, 44, 37, 38, 24, 2, 10, 44]
    build_heap(alist)
    print alist
    alist = [21, 44, 37, 38, 24, 2, 10, 44]
    build_heap(alist, cmp_swap=cmp_swap_max)
    print alist

giving output:
    
    [2, 24, 10, 38, 44, 37, 21, 44]
    [2, 24, 10, 38, 44, 37, 21, 44]
    [44, 44, 37, 38, 24, 2, 10, 21]
"""

#### BUILD HEAP FROM A LIST ####

#Given a list

#downheapify
#
#    if not a leaf
#   	get left and right child
#   	sift down compare and swap inplace
#   	recurse on both left and right
#    else
#   	get the leaf
#        upheapify
#            
#            if not yet root
#                sift up compare and swap inplace
#      		get the parent
#      		recurse on parent
#      	    else
#      		siftup the last root
#############################################################

from collections import deque

def is_leaf(node_index, alist):
    ln = len(alist)
    lchild = 2*node_index + 1
    rchild = lchild + 1
    return not (lchild < ln or rchild < ln)

def cmp_swap_min(alist, parent_index, lchild, rchild, size, ln):
    #if not (parent_index <= size):
    #    return
    greater = smaller = 0
    #print "At parent index {} Comparing parent node {}".format(parent_index, parent_node)
    #chk size overflow
    if lchild < ln:
        #cmp
        if rchild < ln:
            if alist[lchild] > alist[rchild]:
                greater, smaller = lchild, rchild
            else:
                greater, smaller = rchild, lchild
        else:
            smaller = lchild
        if alist[parent_index] > alist[smaller]:
           alist[parent_index], alist[smaller] =  alist[smaller], alist[parent_index]
        """
        #Interchange child nodes IFF they are leaves
        if is_leaf(lchild, alist) and is_leaf(rchild, alist):
            if alist[lchild] == alist[smaller] and rchild < ln:
                alist[lchild], alist[rchild] = alist[greater], alist[smaller]
        """

def cmp_swap_max(alist, parent_index, lchild, rchild, size, ln):
    #if not (parent_index <= size):
    #    return
    parent_node = alist[parent_index]
    #print "At parent index {} Comparing parent node {}".format(parent_index, parent_node)
    #chk size overflow
    if lchild < ln:
        #cmp
        if rchild < ln and alist[rchild] > parent_node and alist[rchild] > alist[lchild]:
            alist[parent_index], alist[rchild] = alist[rchild], alist[parent_index]
        elif alist[lchild] > alist[parent_index]:
            alist[parent_index], alist[lchild] = alist[lchild], alist[parent_index]


def calc_child_nodes(index):
    lchild = 2*index + 1
    rchild = lchild + 1
    return lchild, rchild


def siftup(alist, node, size, ln, cmp_swap):
    lchild, rchild = calc_child_nodes(node)
    cmp_swap(alist, node, lchild, rchild, size, ln)
    return

def upheapify(alist, ln, root, size, cmp_swap):
    if (0 < root < ln):
        #sifting up with compare and swap
        siftup(alist, root, size, ln, cmp_swap)
        #get the parent of the current node
        parent = (root-1)//2
        #recurse
        upheapify(alist, ln, parent, size, cmp_swap)
    else:
        #return and finish when node reaches trees root
        return siftup(alist, root, size, ln, cmp_swap)


def siftdown(alist, root, lchild, rchild, size, ln, cmp_swap):
    return cmp_swap(alist, root, lchild, rchild, size, ln)


def downheapify(alist, ln, root, size, cmp_swap):
    if not is_leaf(root, alist) and (root < ln):
        #get left and right nodes
        lchild, rchild = calc_child_nodes(root)
        #sift down comparing and swapping
        siftdown(alist, root, lchild, rchild, size, ln, cmp_swap)
        #get the leaves of each branch left and right
        downheapify(alist, ln, lchild, size, cmp_swap)
        downheapify(alist, ln, rchild, size, cmp_swap)
    else:
        #get the node that is a leaf if its a leaf overflow
        if not (root<ln):
            root = (root-1)//2
        #Sift up leaf
        return upheapify(alist, ln, root, size, cmp_swap)



def build_heap(alist, start_index = 0, cmp_swap = cmp_swap_min):
    ln = len(alist)
    size = ln//2
    root = start_index
    downheapify(alist, ln, root, size, cmp_swap)
    return alist


#works for deques
def heap_insert(alist, num, cmp_swap):
    alist.append(num)
    return build_heap(alist, cmp_swap = cmp_swap)

def heap_remove_root(alist, cmp_swap):
    alist.popleft()
    alist.appendleft(alist.pop())
    #print alist
    #print
    return build_heap(alist, cmp_swap = cmp_swap)

def heap_sort(alist, cmp_swap):
    """feed in a deque and sort in a new list"""
    l = []
    while len(alist):
        #heapify initially
        alist = build_heap(alist, cmp_swap=cmp_swap)
        l.append(alist.popleft())
    return l


if __name__ == "__main__":
    """
    from copy import deepcopy
    import heapq
    alist = deque([21, 44, 37, 38, 24, 2, 10, 44])
    blist = deepcopy(alist)
    alist = list(alist)
    heapq.heapify(alist)
    blist = build_heap(blist)
    print alist
    print blist
    
    assert alist == list(blist)
    print alist
    print blist
    print
    
    alist = deque([21, 44, 37, 38, 24, 2, 10, 44])
    blist = list(deepcopy(alist))
    build_heap(alist)
    heapq.heapify(blist)
    blist = deque(blist)
    blist.popleft()
    blist.appendleft(blist.pop())
    print blist
    print
    blist = list(blist)
    heapq.heapify(blist)
    print alist
    print
    heap_remove_root(alist, cmp_swap_min)
    print alist
    print blist
    print
    
    alist = deque([21, 44, 37, 38, 24, 2, 10, 44])
    blist = list(deepcopy(alist))
    build_heap(alist)
    heapq.heapify(blist)
    
    heap_insert(alist, 45, cmp_swap_min)
    build_heap(alist)
    blist.append(45)
    heapq.heapify(blist)
    
    print alist
    print blist"""

    import time
    from heapq import heapify, heappush, heappop
    from math import log
    from numpy.random import randint
        
    def heapsort(iterable):
        h = []
        for value in iterable:
            heappush(h, value)
        return [heappop(h) for i in range(len(h))]
    

    
    tmp = []
    for i in xrange(2,1002):
        l = deque(randint(0,i, i))
        ln = len(l)
        start = time.time()
        heap_sort(l, cmp_swap_max)
        end = time.time() - start
        start1 = time.time()
        heapsort(list(l))
        end1 = time.time() - start1
        tmp.append((ln, end, end1, ln*log(ln,2)))