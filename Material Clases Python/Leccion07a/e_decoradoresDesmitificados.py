import time

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


def memoize_any_function(func_to_memoize):
    "Return a wrapped version of the function using memoization"

    def memoized_version_of_func(n):
        "Wrapper using memoization"
        res = cache.get_key(n)
        if res is None:
            res = func_to_memoize(n)  # Call the real function
            cache.set_key(n, res)
        return res
    return memoized_version_of_func

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


fibonacci = memoize_any_function(fibonacci)
factorial = memoize_any_function(factorial)

start = time.time()
fibonacci(35)
print("Elapsed:", time.time() - start)

@memoize_any_function
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@memoize_any_function
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

start = time.time()
fibonacci(35)
print("Elapsed:", time.time() - start)

start = time.time()
print(factorial(4))
print("Elapsed:", time.time() - start)

cache