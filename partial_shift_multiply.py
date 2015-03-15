"""
Multiply any two numbers by:
    1. taking the individual digits out using division and mod
    2. performing partial multiplication and multiplying by 10**n-1
    where n is the total length of the number string;
    3. adding all product outputs.
"""

def partial_shift_multiply(target, num):
    """
    A typical multiplication by hand operation
    shone here that takes 2mn time generally to perform
    or if m=n then 2n^2.
    Thus it is a Quadratic time operation.
    NOTE: Each Iteration is independent and THUS can be made parallel.
    Thus, in parallel it is at max of the Order O(n) = 2n.
    """
    res = 0
    #get the length
    ln = len(str(num))
    #iter over the multiplier digits
    for i in xrange(ln-1, -1, -1):
        x = ln - i
        j = 10**(x - 1)  #OR ln - (i+1)
        single = (num%10**x)/j
        #print single * j
        #multiply with multiplicant and shift by j
        res += target * single * j
    #doing all iterations over m numbers makes it 2n*m or 2n^2 if m=n
    return res
