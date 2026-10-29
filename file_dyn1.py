# dynamic programming basics
#

from time import perf_counter
from functools import cache
from typing import Callable

@cache # memoization
def Find_Fibbo(nth: int) -> int: return nth if nth in (0, 1) else Find_Fibbo(nth - 1) + Find_Fibbo(nth - 2)

def Find_Fibbo2(n: int) -> int:
    # by using tabulation
    #

    if n in (0, 1): return n

    dp = [0] * n
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n): dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]

def Find_Fibbo3(n: int, cache: dict | None = None) -> int:
    # by using memoization
    #
    # roughly equivalent to Find_Fibbo

    if not cache: cache = { 0: 1, 1: 1 }
    if cache.get(n): return cache[n]

    cache[n] = Find_Fibbo3(n - 1, cache) + Find_Fibbo3(n - 2, cache)
    return cache[n]



def timer(fn: Callable):
    def inner(*args, **kwargs):
        start = perf_counter()
        _ = fn(*args, **kwargs)
        time_taken = perf_counter() - start

        print(f"The total time taken is {time_taken} seconds.")

    return inner

@timer
def calc_fibbos(n: int):
    for i in range(n): print(Find_Fibbo3(i))
