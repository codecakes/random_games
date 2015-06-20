from collections import defaultdict

def int_repeating_pattern(alist):
    l = defaultdict(int)
    prev = ''
    for num in alist:
        prev += str(num)
        l[int(prev)] += 1
        sym1, sym2 = int(prev[:len(prev)//2]), int(prev[len(prev)//2:])
        if sym1 == sym2 and sym1 in l:
            l[sym1] += 1
    return l

def list_pattern(alist):
    l = defaultdict(int)
    prev = []
    single = []
    for num in alist:
        single.append(num)
        if prev:
            prev.append(prev[-1] + [num])
            l[tuple(prev[-1] + [num])] += 1
        else:
            prev.append([num])
            l[tuple([num])] += 1
    return prev, l