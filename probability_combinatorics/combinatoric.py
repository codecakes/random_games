from decimal import Decimal
from math import e, factorial

def combination(num, den):
    """
    Find nCr or (n r), the Binomial Coefficients
    """
    dec1 = dec2 = Decimal(1)
    if 0 <= den <= num:
        diff = num - den
        if num-diff < num-den:
            temp = diff
            other = den
        else:
            temp = den
            other = diff
        for _ in xrange(num-temp):
            dec1 *= num
            num -= 1
        for _ in xrange(other):
            dec2 *= other
            other -= 1
        del temp, other, diff
        return dec1/dec2


def permutation(num, den):
    """
    Find nPr
    """
    dec1 = dec2 = Decimal(1)
    if 0 <= den <= num:
        for _ in xrange(den):
            dec1 *= num
            num -= 1
        return dec1

def binomial_probability_distro(n, r, p):
    return float(combination(n, r)) * p**n * (1-p)**(n-r)

expected_value = lambda k, n, r, p: k * binomial_probability_distro(n,r,p)

def total_expected_value(n, p):
    return sum([expected_value(k, n, k, p) for k in xrange(1, n+1)])

def poisson_value(Y, r):
    """
    Given Expected Value E(X) = Y = n(num of trails) * p (Probability)
    p = Y/n;
    Probability of Event X happening = (n r)(Y/n)**r * (1- Y/n)**(n-r) = Y**r/r! * e**-Y
    """
    return (float(Y**r)/factorial(r)) * e**(-Y)
