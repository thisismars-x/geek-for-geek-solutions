# prefix sum
#
# Many solutions here can be weird, why is prefix calculated when we are serving only
# a single range query. This is just to simplify things, in real world, this should not be done.

from itertools import accumulate
from typing import Callable

from misc import Print_Matrix

def Equilibrium_Index(numbers: list[int]) -> int:
    n = len(numbers)
    pre_sum = [0] * n
    pre_sum[0] = numbers[0]

    for i in range(1, n):
        pre_sum[i] = pre_sum[i - 1] + numbers[i]

    for i in range(n - 1):
        if pre_sum[i] == pre_sum[n - 1] - pre_sum[i + 1]:
            return i + 1

    return -1

def Subarray_With_0Sum(numbers: list[int]) -> bool:
    n = len(numbers)
    sums = set()

    pre_sum = numbers[0]
    sums.add(pre_sum)

    for i in range(1, n):
        pre_sum += numbers[i]
        if pre_sum in sums: return True
        sums.add(pre_sum)

    return False

    # naive solution
    # n = len(numbers)

    # for i in range(n):
    #     for j in range(i, n):
    #         if sum(numbers[i: j + 1]) == 0: return True

    # return False

def Maximum_Subarray_Size_Sum_Lt_K(numbers: list[int], k: int) -> int:
    n = len(numbers)

    start, end = 0, 0
    minlen = n

    curr_sum = 0
    while end < n:
        curr_sum += numbers[end]

        while curr_sum > k:
            curr_sum -= numbers[start]
            minlen = min(minlen, end - start)
            start += 1

        end += 1

    return minlen


def Prefix_Sum_2D_Matrix(matrix: list[list[int]], *, show = False) -> list[list[int]]:
    if show:
        print("Input Matrix:")
        Print_Matrix(matrix)

    r, c = len(matrix), len(matrix[0])

    pre_sum: list[list[int]] = [ [0] * c for _ in range(r) ]

    for i in range(r):
        for j in range(c):
            tmp_sum = matrix[i][j]
            if j - 1 >= 0: tmp_sum += pre_sum[i][j-1]
            if i - 1 >= 0: tmp_sum += pre_sum[i-1][j]
            if i - 1 >= 0 and j - 1 >= 0: tmp_sum -= pre_sum[i-1][j-1]

            pre_sum[i][j] = tmp_sum

    if show:
        print("\nPresum Matrix:")
        Print_Matrix(pre_sum)
    return pre_sum


def Range_Sum(numbers: list[int]) -> Callable[[int, int], int]:
    n = len(numbers)
    pre_sum = [0] * n
    pre_sum[0] = numbers[0]
    for i in range(1, n): pre_sum[i] += pre_sum[i - 1] + numbers[i]

    def answer_range_queries(i: int, j: int) -> int: return pre_sum[j] - (pre_sum[i - 1] if i > 0 else 0)
    return answer_range_queries


def Mean_Of_Range(numbers: list[int], i: int, j: int) -> int:
    n = len(numbers)
    pre_sum = [numbers[0], *(0 for _ in range(n - 1))]
    for _i in range(1, n): pre_sum[_i] = pre_sum[_i - 1] + numbers[_i]

    return (pre_sum[j] - (pre_sum[i - 1] if i - 1 >= 0 else 0) ) // (j - i + 1)


def Check_Possible_Split(numbers: list[int]) -> bool:
    pre_sums = list(accumulate(numbers))
    found_sums = set(pre_sums)

    return pre_sums[-1] // 2 in found_sums
