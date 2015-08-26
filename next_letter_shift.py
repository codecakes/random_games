# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):
    return chr(((ord(letter) - 97 + 1) % 26) + 97)

    
    


assert shift('a') == 'b'

assert shift('n') == 'o'

assert shift('z') == 'a'

# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    return chr(((ord(letter) - 97 + n) % 26) + 97)



assert shift_n_letters('s', 1) == 't'

assert shift_n_letters('s', 2) == 'u'

assert shift_n_letters('s', 10) == 'c'

assert shift_n_letters('s', -10) == 'i'

def rotate(line, n):
    # Your code here
    split_list = line.split()
    return ' '.join(map(lambda each_str: ''.join(map(lambda lt: shift_n_letters(lt, n), \
                                    each_str)), split_list))

print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
