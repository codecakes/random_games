def merge_split(op, perms, res):
    """
    #merge_split({1,2,3,4}, [], [])
    """
    if op:
        #O(n) each level
        for pos,lt in enumerate(op):
            print "lt {} op {}".format(lt, op)
            print "splitting {} merging {} \nmaster list {}\n".format(op- {lt}, [lt]+perms, res)
            merge_split(op- {lt}, perms+[lt], res, level=level)
    else:
        res.append(perms)
    return res

