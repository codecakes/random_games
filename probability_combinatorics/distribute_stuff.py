def distribute_something(count, people):
    """
    Given count = X things
    distribute it among people=N
    """
    l = [0] * people
    while count > 0:
        for i in xrange(len(l)):
            l[i] += 1
            count -= 1
            if count == 0: return l
