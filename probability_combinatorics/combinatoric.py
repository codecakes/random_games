def combination(num, den):
    """
    Find nCr or (n r)
    """
    dec1 = dec2 = 1
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
        return float(dec1)/dec2
