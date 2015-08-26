def cached_execution(cache, proc, proc_input):
    if proc in cache:
        if proc_input in cache[proc]:
            return cache[proc][proc_input]
    res = proc(proc_input)
    cache.setdefault(proc, {})[proc_input] = res
    return res

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
def cached_fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return cached_execution(cache,  cached_fibo, n - 1 ) + \
        cached_execution(cache,  cached_fibo, n - 2 )

def cached_fibo2(n):
    if n == 1 or n == 0:
        return n
    else:
        return cached_execution(cache,  cached_fibo, n - 1 ) + \
        cached_execution(cache,  cached_fibo, n - 2 )

cache = {}
print cached_execution(cache, cached_fibo, 100)

import time

start = time.clock()
cached_fibo(100)
print time.clock() - start

start = time.clock()
cached_execution(cache, cached_fibo, 100)
print time.clock() - start

start = time.clock()
cached_execution(cache, cached_fibo2, 100)
print time.clock() - start
