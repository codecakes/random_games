#another way of doing recursive palindrome
def is_palindrome(s):
    ln = len(s)
    if s != '':
        if s[ln-1] == s[0]:
            return True and is_palindrome(s[1:ln-1])
        return False
    return True

assert is_palindrome('abab') == False
assert is_palindrome('abba') == True
assert is_palindrome('madam') == True
assert is_palindrome('madame') == False
assert is_palindrome('') == True

#non recursive loop method
def is_palindrome_loop(s):
    ln = len(s)
    stat = True
    for i in xrange(ln/2):
        stat = stat and (s[i] == s[ln-i-1])
        if not stat:
            return False
    return True

assert is_palindrome_loop('abab') == False
assert is_palindrome_loop('abba') == True
assert is_palindrome_loop('madam') == True
assert is_palindrome_loop('madame') == False
assert is_palindrome_loop('') == True

#easier pythonic way
def is_pal_easy(s): return s == s[::-1]

assert is_pal_easy('abab') == False
assert is_pal_easy('abba') == True
assert is_pal_easy('madam') == True
assert is_pal_easy('madame') == False
assert is_pal_easy('') == True
