def max_val_rec(alist):
    """
    For 1D array
    What if there is unsorted array?
    I doubt Binary Search would work.
    Doing a max peak value search by recursive divide.
    Not Binary Search.
    """
    ln = len(alist)
    mid = ln//2
    if ln > 2:
        left = max_val_rec(alist[:mid])
        right = max_val_rec(alist[mid:])
        return max(left, right)
    else:
        return max(alist)

def max_val_rec_2d(arr):
    """
    For 2D array
    What if there is unsorted array matrix?
    I doubt Greedy Ascent would work.
    Breaking in O(n) time each row
    and THEN
    Doing a max peak value search by recursive divide,
    using max_val_rec should make it O(nlogn);
    """
    return max_val_rec([max_val_rec(each_list) for each_list in arr])


if __name__ == "__main__":
    import time
    n = 0
    tmp = []
for i in xrange(2, 1002):
    up = randint(2, i+1)
    alist = [randint(1,up) for _ in xrange(i)]
    assert max(alist) == max_val_rec(alist)
    n = len(alist)
    start = time.time()
    max_val_rec(alist)
    end = time.time() - start
    tmp.append((n, end))
    tmp = sorted(tmp, key= lambda x: x[1])
    x,y = zip(*tmp)
    #and now you can plot using matplotlib