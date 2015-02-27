"""
Uncomment to see the flow of Operation.
"""

from math import sqrt
from numpy import inf

dist = lambda p1,p2: sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)
    
def bfd(alist):
    """
    Given a presorted list in increasing order by x axis,
    returns the minimum distance and its pair among the points.
    alist: a list of (x,y) points
    """
    ln = len(alist)
    min_d = inf
    
    for pre_indx in xrange(ln-1):
        for post_indx in xrange(pre_indx+1, ln):
            p1, p2 = alist[pre_indx], alist[post_indx]
            ds = dist(p1, p2)
            if ds < min_d:
                min_d = ds
                pair = p1, p2
    #print "min_d, pair: {} {}\nbfd list: {}\n".format(min_d, pair, alist)
    return min_d, pair
                 
    
def alist_merge(left_list, right_list):
    """
    returns the distance between the adjoining joints of the two lists and its pair
    """
    ds = dist(left_list[-1], right_list[0])
    return ds, (left_list[-1], right_list[0])


def split_conquer(alist):
    """
    gets a presorted list
    returns the minimum distance and its resp. pair points.
    A pair is a Pair of 2 points.
    """    
    ln = len(alist)    
    #divide recursively
    mid = ln//2
    
    #until len is not greater than 3 - Base Case
    if ln <= 3:
        #find the min distance between the 2 points using brute force 
        #and return the min_d and point pair
        #print "list going in bfd {}\n".format(alist)
        min_d, pair = bfd(alist)
        return min_d, pair
    else:
        #print "Splitting {}\n".format(alist)
        left_list = alist[:mid]
        left_min_d, left_pair = split_conquer(left_list)
        right_list = alist[mid:]
        right_min_d, right_pair = split_conquer(right_list)
        
        #merge two lists of len 2 or less
        #find the min distance between these two merged lists at the mid joint point
        joint_min, joint_pair = alist_merge(left_list, right_list)
        
        #find overall min distance - delta
        delta = min(left_min_d, joint_min, right_min_d)
        if delta == left_min_d:
            delta_pair = left_pair
        elif delta == right_min_d:
            delta_pair = right_pair
        else:
            delta_pair = joint_pair
        
        ## Whole Point of Above is to get the "mid point" AND "delta" min val ##
        #Now we find xbase_delta i.e. for mid +/- xbase_delta
        xbase_delta = (delta_pair[1][0] - delta_pair[0][0])
        
        #Now for filter all the points within (mid +/- xbase_delta) by x
        #Using Brute Force, find the min of all those filtered points and previous min
        #print "Points being filtered {}\n".format(alist)
        #print "mid - delta {} mid + delta {}\n".format(alist[mid][0] - xbase_delta, alist[mid][0] + xbase_delta)
        
        filtered_pts = filter(lambda points: \
        (alist[mid][0] - xbase_delta <= points[0] <= alist[mid][0])\
        or (alist[mid][0] <= points[0] <= alist[mid][0] + xbase_delta), alist)
        
        #print "filtered_pts:{}\n".format(filtered_pts)
        if len(filtered_pts)==1:
            return inf, filtered_pts[0]
        
        filtered_min, pair = bfd(filtered_pts)
        
        #print "current MINIMUM {}\n".format(filtered_min)
        
        #return this min distance and the point pair
        return (filtered_min, pair) \
        if min(filtered_min, delta) == filtered_min else (delta, delta_pair)

if __name__ == "__main__":
    from numpy.random import randint
    from cProfile import run
    import time
    from matplotlib.pyplot import plot
    #alist = [(9, 0), (7, 0), (6, 2), (3, 6), (4, 2), (4, 3), (2, 0), (4, 5), (1, 3), (2, 6)]
    tmp = []
    for n in xrange(11, 1000):
        up_bound = randint(1,n)
        alist = [(randint(0,up_bound),randint(0,up_bound)) for _ in xrange(n)]
        x,y = zip(*sorted(alist, key =lambda i: i[0]))
        alist = zip(x,y)
        #print bfd(alist)
        #print "sorted list: {}\n".format(alist)
        start = time.time()
        #run("split_conquer(alist)")
        #print split_conquer(alist)
        end=time.time()-start
        #print "finished in {}\n".format(end)
        tmp.append((len(alist), end))
    
    size, tym = zip(*tmp)
    #interestingly it did scale
    plot(size, tym)