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

#Step 1: check if its a leaf

# Step 2: if No Then cmp its L & R child Nodes and swap w/ greater one
#   2.1 Go down to L & recurse from Step 1
#   2.1 Go down to R & recurse from Step 1

# Step 3: Else cmp w/ parent and swap w/ greater one
#   3.1 Ret back to Parent
#   3.2 If Parent is Root - STOP Else Go to Step 3


def is_leaf(node_index, alist):
    ln = len(alist)
    lchild = 2*node_index + 1
    rchild = lchild + 1
    return not (lchild < ln or rchild < ln)

def cmp_swap_min(alist, parent_index, lchild, rchild, size, ln):
    if not (parent_index <= size):
        return
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
    #print "alist {}".format(alist)

def cmp_swap_max(alist, parent_index, lchild, rchild, size, ln):
    if not (parent_index <= size):
        return
    parent_node = alist[parent_index]
    #print "At parent index {} Comparing parent node {}".format(parent_index, parent_node)
    #chk size overflow
    if lchild < ln:
        #cmp
        if rchild < ln and alist[rchild] > parent_node and alist[rchild] > alist[lchild]:
            alist[parent_index], alist[rchild] = alist[rchild], alist[parent_index]
        elif alist[lchild] > alist[parent_index]:
            alist[parent_index], alist[lchild] = alist[lchild], alist[parent_index]
    #print "alist {}".format(alist)

    
def heapify(alist, size, ln, cmp_swap, index=0):
    #adhere to heap property
    if (0 <= index < size):
        #print "comparing down list {}".format(alist)
        lparent = 2*index + 1
        rparent = lparent + 1
        cmp_swap(alist, index, lparent, rparent, size, ln)
        heapify(alist, size, ln, cmp_swap, index= lparent)
        heapify(alist, size, ln, cmp_swap, index= rparent)
    index //= 2
    lparent = 2*index + 1
    rparent = lparent + 1
    cmp_swap(alist, index, lparent, rparent, size, ln)
    return

def build_heap(alist, cmp_swap = cmp_swap_min):
    ln = len(alist)
    size = ln//2
    heapify(alist, size, ln, cmp_swap, index=0)
    return alist
