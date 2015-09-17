# Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. It can 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement): 
    return (match, replacement)

#iterative soln - first gross attempt
def apply_converter(converter, string):
    '''Recursive replace operation on a keyword'''
    assert len(converter[0]) >= len(converter[1])
    res = string
    s= ''
    #Get length of matching substring
    ln_match = len(converter[0])
    #Get length of the current full string
    str_ln = len(res)
    count = 0
    
    #while the index count < full string length #O(N)
    while count < str_ln:
        s += res[count]
        #print "count is %s s is %s" %(count, s)
        #if there's a match
        if len(s) == ln_match:
            #if substr is the matching string
            if s == converter[0]:
                #Replace everything upto that count with the replacement and append the rest of full string
                res = res[:count+1].replace(s, converter[1]) + res[count+1:]
                s = ''  #reset
                #print "IF block res: %s" %res
                str_ln = len(res)  #get new fulll string length
                count = 0  #start again
                continue
            else:
                count = count - ln_match + 2
                s = ''
        else:
            count += 1
        #print "res is %s count is %s" %(res, count)
    return res

#recursive soln - elegant soln
def apply_converter(converter, string):
    new_str = string.replace(converter[0], converter[1])
    return apply_converter(converter, new_str) \
    if new_str.find(converter[0]) != -1 else new_str

#iterative soln- elegant soln
def apply_converter(converter, string):
    '''Recursive replace operation on a keyword'''
    assert len(converter[0]) >= len(converter[1])
    prev_str = None
    substr_match = len(converter[0])
    while prev_str != string:
        prev_str = string
        match_pos = string.find(converter[0])
        if match_pos != -1:
            string = string[:match_pos] + converter[1] + \
                        string[match_pos+substr_match:]
    return string


# For example,

#Reductionist examples
c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
#>>> ab

#Non reductionist
c = make_converter('a', 'aa')
#print apply_converter(c, 'a')
# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would 
# run forever).