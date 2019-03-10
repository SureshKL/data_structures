"""
Fibonacci series: 1 1 2 3 5 8

Dynamic Programming is a technique where recurring sub problems results are
retrieved from cache to speed up execution.

Look at the performance improvement after applying caching for recursion.
"""
import time
from functools import wraps


def time_taken(func, *args, **kwargs):
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    print(f'{func.__name__} took {end_time - start_time} secs')
    return result


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper


def fibonacci_recursion(num):
    """Get fibonacci number"""
    if num == 1 or num == 2:
        return 1
    return fibonacci_recursion(num - 1) + fibonacci_recursion(num - 2)

@memoize
def fibonacci_recursion_with_memoize(num):
    """Get fibonacci number"""
    if num == 1 or num == 2:
        return 1
    return fibonacci_recursion_with_memoize(num - 1) + fibonacci_recursion_with_memoize(num - 2)


def fibonacci_dynamic_program(num, lookup):
    """Get fibonacci number"""
    if num == 1 or num == 2:
        lookup[num] = 1

    if lookup[num] is None:
        lookup[num] = fibonacci_dynamic_program(
            num - 1, lookup) + fibonacci_dynamic_program(
            num - 2, lookup)

    return lookup[num]


def fibonacci_bottom_up_approach(num):
    """Get fibonacci series"""
    if num == 1:
        return [1]

    series = [1, 1, ]
    for i in range(2, num):
        series.append(series[i - 1] + series[i - 2])
    return series


def fibonacci_generator(num):
    """Get fibonacci series"""
    a = b = 1
    for i in range(2, num + 2):
        if i == 1 or i == 2:
            yield 1
        else:
            yield b
            a, b = b, b + a


if __name__ == '__main__':
    print(time_taken(fibonacci_recursion, 35))
    print(time_taken(fibonacci_recursion_with_memoize, 35))
    n = 35
    lookup = [None] * (n + 1)
    print(time_taken(fibonacci_dynamic_program, n, lookup))
    print(time_taken(fibonacci_bottom_up_approach, 35)[-1])
    print(list(time_taken(fibonacci_generator, 35))[-1])
