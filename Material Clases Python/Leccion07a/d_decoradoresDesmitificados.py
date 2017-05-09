"""

"""
import time

def factorial(n):
    "Return n! (the factorial of n): n! = n * (n-1)!"
    if n < 2:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    "Return nth fibonacci number: fib(n) = fib(n-1) + fib(n-2)"
    if n < 2:
            return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(list(map(factorial, range(10))))
print(list(map(fibonacci, range(10))))


start = time.time()
fibonacci(35)
print("Elapsed:", time.time() - start)

"""

"""
import Leccion07a.cache as cache
def fibonacci(n):
    "Return nth fibonacci number: fib(n) = fib(n-1) + fib(n-2)"
    if n < 2:
        return n
    fib = cache.get_key(n)
    if fib is None:
        fib = fibonacci(n - 1) + fibonacci(n - 2)
        cache.set_key(n, fib)
    return fib

start = time.time()
fibonacci(35)
print("Elapsed:", time.time() - start)

"""

"""
def fibonacci(n): # The function remains unchanged
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

real_fibonacci = fibonacci
def fibonacci(n):
    fib = cache.get_key(n)
    if fib is None:
        fib = real_fibonacci(n)
        cache.set_key(n, fib)
    return fib

start = time.time()
fibonacci(35)
print("Ha tardardo %.6e s" %(time.time()-start,) )