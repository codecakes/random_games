#fib loop
def fibonacci(n):
    prev = 0
    now = 1
    while n:
        prev, now = now, now + prev
        n -= 1
    return prev

assert fibonacci(0)==0
assert fibonacci(1)==1
assert fibonacci(15)==610

#fib recursive
def rec_fib(n):
    return rec_fib(n-1) + rec_fib(n-2) if n > 1 else n

assert rec_fib(0)==0
assert rec_fib(1)==1
assert rec_fib(15)==610
