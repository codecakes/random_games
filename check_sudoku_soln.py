def check_sudoku(list_of_lists):
    index = (0,0)
    N = len(list_of_lists[0])
    #O(N^3)
    for r in xrange(N):
        for c in xrange(N):
            index = (r,c)
            #check col wise
            for each_list_index in xrange(N):
                if (each_list_index, c) != index and \
                list_of_lists[each_list_index][c] == list_of_lists[r][c]:
                    return False
            #col row wise
            for each_col_index in xrange(N):
                if (r, each_col_index) != index and \
                list_of_lists[r][each_col_index] == list_of_lists[r][c]:
                    return False
    return True