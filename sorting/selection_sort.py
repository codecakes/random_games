def selection_sort(n_arr):
    #O(n^2)
    min_val_store = cur_val = cur_iter_pos = cur_min_pos = 0
    for pos, val in enumerate(n_arr):
        cur_iter_pos, cur_val = pos, val
        min_val_store = cur_val
        for min_pos, min_val in enumerate(n_arr[cur_iter_pos+1:]):
            if min_val < min_val_store:
                cur_min_pos = cur_iter_pos+min_pos+1
                min_val_store = min_val
        #print "cur_iter_pos {} cur_min_pos {}".format(cur_iter_pos,cur_min_pos)
        #print "cur_val {} min_val {}".format(n_arr[cur_iter_pos], n_arr[cur_min_pos])
        if min_val_store != cur_val:
            #then swap
            n_arr[cur_iter_pos], n_arr[cur_min_pos] = min_val_store, cur_val
        cur_min_pos = 0
    return n_arr

#just for testing
if __name__ == "__main__":
    for _ in xrange(10):
        arr = [randint(-3789,1001) for _ in xrange(10)]
        assert all(sort(arr) == selection_sort(arr))
