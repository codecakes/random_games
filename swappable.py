# -*- coding: utf-8 -*-
"""
Problem: You are given an integer m (1 ¬ m ¬ 1 000 000) and two non-empty, zero-indexed
arrays A and B of n integers, a0, a1, . . . , an−1 and b0, b1, . . . , bn−1 respectively (0 ¬ ai
, bi ¬ m).
The goal is to check whether there is a swap operation which can be performed on these
arrays in such a way that the sum of elements in array A equals the sum of elements in
array B after the swap. By swap operation we mean picking one element from array A and
one element from array B and exchanging them.

Solution O(n2): The simplest method is to swap every pair of elements and calculate the
totals. Using that approach gives us O(n
3
) time complexity. A better approach is to calculate
the sums of elements at the beginning, and check only how the totals change during the swap
operation.
2.2: Swap the elements — O(n
2
).
1 def slow_solution(A, B, m):
2 n = len(A)
3 sum_a = sum(A)
4 sum_b = sum(B)
5 for i in xrange(n):
6 for j in xrange(n):
7 change = B[j] - A[i]
8 sum_a += change
9 sum_b -= change
10 if sum_a == sum_b:
11 return True
12 sum_a -= change
13 sum_b += change
14 return False
"""
from numpy.random import randint

def gen_unique_arr(low, up, limit):
    l = []
    for _ in xrange(limit):
        r = randint(low, up)
        while r in l:
            r = randint(low, up)
        l.append(r)
    return l

    

def counting(A, m):
    # m = max(A) => O(N)
    n = len(A)
    count = [0] * (m + 1)  #includes list uptil max(A) + [0]
    for k in xrange(n):
        count[A[k]] += 1
    return count

def swappable(A,B):
    #A and B are two lists of same length
    #print max(A), max(B)
    mA, mB = max(A), max(B)  #O(N)
    C,D = (B,A) if mA > mB else (A,B)
    sD, sC  = sum(D), sum(C)
    d = abs(sD- sC)
    #print "sC {}, sD {}".format(sC, sD)
    #print "d {}".format(d)
    if d % 2 == 1: return False
    d //= 2
    m = max(D)
    count = counting(D, m) #if sA > sB else counting(B, max(B))#O(mA)
    #print "C {}, D {}".format(C, D)
    
    for num in C:
        res_num = num + d
        #print res_num
        if 0 <= res_num <= m:
            if count[res_num] == 1 and (sC + res_num - num) == (sD + num - res_num):
                print "A {} - B {}".format(num if C==A else res_num, res_num if D==B else num)
                return True
    return False