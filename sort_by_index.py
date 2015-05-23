# -*- coding: utf-8 -*-
"""
Problem Statement

You are given data in a tabular format i.e. the data contains N rows and each row contains M space-separated elements.

You can imagine the M items to be different attributes (like height, weight, energy, etc) and each of the N rows as an instance or a sample.

Your task is to sort the table on the Kth attribute and print the final resulting table.

[If two attributes are the same for different rows, print the row that appeared first in the input]

Input Format First line contains N and M separated by a space. 
Next N lines contain M elements each. 
The last line contains K.

Constraints 
1≤N,M≤1000 
0≤K<M 
each element ≤1000
Output Format 
Print the N lines of the sorted table, each line has space-separated elements. Check the sample below for clarity.

Sample Input

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
Explanation 
The table is sorted on the second attribute shown as K=1 (because it's 0-indexed).
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from operator import itemgetter

N,M = map(int, raw_input().split())

if N>=1 and M<= 1000:
    res = []
    for _ in xrange(N):
        lst = []
        inp = (raw_input().split())
        if len(inp) == M:
            for i in inp:
                x = int(i)
                if x <= 1000: lst.append(x)
            res.append(lst)


    k_pos = int(raw_input())
    if 0<= k_pos <= M:
        res.sort(key=itemgetter(k_pos))
        for each in res:
            print ' '.join(map(str, each))    