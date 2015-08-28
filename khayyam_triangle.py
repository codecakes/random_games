# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.

def fn(proc, *args, **kwargs):
    cache = proc.cache = {}
    def cached_exec(*args, **kwargs):
        if proc in cache:
            if args in cache[proc]:
                return cache[proc][args]
        res = proc(args[0])
        cache.setdefault(proc, {})[args] = res
        return res
    return cached_exec

@fn
def fact(n):
    res = 1
    count = 1
    while n:
        res *= count
        count += 1
        n -= 1
    return res

def combination(n,k):
    return fact(n)/(fact(k) *(fact(n-k))) if n >= k else 0

def triangle(n):
    return [[combination(each_row, k) for k in xrange(each_row+1)] for each_row in xrange(n)]
        



#Tests

assert triangle(0) == []

assert triangle(1) == [[1]]

assert triangle(2) == [[1], [1, 1]]

assert triangle(3) == [[1], [1, 1], [1, 2, 1]]

assert triangle(6) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
