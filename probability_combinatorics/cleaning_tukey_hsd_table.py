"""
cleaning Studentized Tukey HSD Table
and turning it into a standard formatted csv table
"""
from cStringIO import StringIO
from collections import defaultdict
import requests
from pandas import DataFrame

r=requests.get('http://cse.niaes.affrc.go.jp/miwa/probcalc/s-range/srng_tbl.html').text
r = r[r.find('-'):r.rfind('-')+1]


alpha_lists = []
temp = []
for line in StringIO(r).readlines():
    t = line.split()
    if t and isinstance(t, list):
        first = t[0]
        if not (first.startswith('-') or first.startswith('df') or first.startswith('The') or first.startswith('<a')):
            if first == '1':
                if temp: alpha_lists.append(temp)
                temp = []
                temp.append(t)
            else:
                temp.append(t)
alpha_lists.append(temp)
del temp

l = []
t = alpha_lists[2][0][1].split('.')
for i in xrange(len(t)+1):
    if i >= len(t):
        l[-2] = ('.'.join([l[i-2],l[i-1]]))
    else:
        num_str = t[i]
        if len(num_str) == 6:
            x,y = num_str[:3], num_str[3:]
            if l:
                l[-1] = '.'.join([l[-1],x])
                l.append(y)
        else: l.append(num_str)

alpha_lists[2][0] = [alpha_lists[2][0][0]] + l[:-1]

table = defaultdict(dict)
count = xrange(2, 21)
#numbers = range(1,21)
for each_list_per in izip(alpha_lists, (.10, .05, .01)):
    each_list, per = each_list_per
    table[per] = defaultdict(dict)
    [table[per][int(each_seg[0])].update(dict(zip(count, map(float,each_seg[1:])))) if each_seg[0] != 'Inf' else table[per]['inf'].update(dict(zip(count, map(float,each_seg[1:])))) for each_seg in each_list]

df = DataFrame(table)
df.to_pickle('q_table')
#df.to_csv('q_table.csv')
