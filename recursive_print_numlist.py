def rec_print(alist):
    """Print HackerShip or its parts if any number is %5 or %3"""
    ln = len(alist)
    mid = ln/2
    if ln > 1:
        left, right = alist[:mid], alist[mid:]
        rec_print(left)
        rec_print(right)
    elif ln == 1:
	#print alist
        num5, num3 = alist[0]%5, alist[0]%3
        if num5==0 and num3==0:
            print "HackerShip"
        elif num5 == 0:
            print "Ship"
        elif num3 == 0:
            print "Hacker"
    return

if __name__ == "__main__":
    r = range(1,101)
    rec_print(r)