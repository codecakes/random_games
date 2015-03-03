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
        return left if left > right else right
    else:
        return max(alist)


def max_val_rec_2d(arr):
    """
    For 2D array
    What if there is unsorted array matrix?
    I doubt Greedy Ascent would work, efficiently.
    Breaking in O(n) time each row
    and THEN
    Doing a max peak value search by recursive divide,
    using max_val_rec should make it O(n)+O(nlogn);
    """
    return max_val_rec([max_val_rec(each_list) for each_list in arr])

def max_val_rec_2d_fast(arr):
    """
    For NxN 2D matrix using numpy 2D array. 
    because indexing is easier and faster.
    Splitting by half just liek in 1D case.
    See max_val_rec for that.
    and THEN
    Doing a max peak value search by recursive divide,
    using max_val_rec should make it O(logn);
    and Total Order is - O(log col.log row)
    """
    shape = arr.shape
    mid = shape[1]//2
    if mid > 0:    
        left = max_val_rec_2d_fast(arr[:, :mid])
        right = max_val_rec_2d_fast(arr[:, mid:])
        return left if left > right else right
    else:
        return max_val_rec(arr[:,0])
        


if __name__ == "__main__":
    import time
    import numpy as np
    from numpy.random import randint
    """
    #For 1D
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
    """
    n = 0
    tmp = []
    for i in xrange(2, 400):
        up = randint(2, i+1)
        mat_arr=randint(up, i+up, size=(i,i))
        assert mat_arr.max() == max_val_rec_2d_fast(mat_arr)
        start = time.time()
        max_val_rec_2d_fast(mat_arr)
        end = time.time() - start
        n = mat_arr.shape[0]
        tmp.append((n, (np.log2(n))**2, end))
    tmp = sorted(tmp, key= lambda x: x[0])
    x,y,z = zip(*tmp)
    #and now you can plot using matplotlib
        
        
    