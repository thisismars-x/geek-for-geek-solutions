# bit manipulation

def Max_Consecutive_Ones(numbers: list[int]) -> int:
    n = len(numbers)
    max_n_1s = 0
    max_n_0s = 0

    curr_n_1s = 0
    curr_n_0s = 0
    for i in range(n):
        if numbers[i] == 1:
            curr_n_1s += 1
            max_n_1s = max(max_n_1s, curr_n_1s)
            curr_n_0s = 0
        else:
            curr_n_0s += 1
            max_n_0s = max(max_n_0s, curr_n_0s)
            curr_n_1s = 0

    return max(max_n_0s, max_n_1s)

def Missing_Number(numbers: list[int]) -> int:
    n = len(numbers)
    return (n + 1) * (n + 2) // 2 - sum(numbers)


from operator import xor
from functools import reduce

def Number_Occuring_Odd_Ntimes(numbers: list[int]) -> int: return reduce(xor, numbers)
