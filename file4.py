# sliding window
#
from collections import Counter, deque
from reprlib import repr as repr_
from sys import maxsize
import sys

def Max_Sum_Subarray(numbers: list[int], k: int) -> int:
    if len(numbers) < k: raise ValueError(f"List = {repr_(numbers)} has size = {len(numbers)} which is less than window size = {k}.")
    curr_sum = max_sum = sum(numbers[:k])
    for i in range(1, len(numbers) - k + 1):
        curr_sum = curr_sum - numbers[i - 1] + numbers[i + k - 1]
        max_sum = max(max_sum, curr_sum)

    return max_sum

def Count_Distinct(numbers: list[int], k: int) -> list[int]:
    res = []

    n = len(numbers)
    # lets maintain a hash table of size 'k'
    counter = Counter(numbers[:k])
    res.append(len(counter))

    for i in range(1, n - k + 1):
        if (previous := numbers[i - 1]) in counter:
            counter[previous] -= 1
            if counter[previous] == 0: counter.pop(previous)
        counter[numbers[i + k - 1]] += 1
        res.append(len(counter))

    return res

def Find_Maximum_Mex_From_Subarrays(numbers: list[int], k: int) -> int:
    max_mex = -maxsize

    n = len(numbers)

    for i in range(n - k + 1):
        small_array = sorted(numbers[i: i + k])
        biggest = small_array[-1]

        small_set = set(small_array)
        for i in range(1, biggest + 1 + 1):
            if i not in small_set:
                max_mex = max(max_mex, i)
                break

    return max_mex

def Minimum_Swaps_To_Group_1s(numbers: list[int]) -> int:
    min_swaps = n = len(numbers)
    if (total_number_of_1s := numbers.count(1)) == 0: return -1

    total_number_of_1s_currently = numbers[:total_number_of_1s].count(1)
    min_swaps = total_number_of_1s - total_number_of_1s_currently

    for i in range(1, n - total_number_of_1s + 1):
        total_number_of_1s_currently = total_number_of_1s_currently - (1 if numbers[i - 1] == 1 else 0) + (1 if numbers[i + total_number_of_1s - 1] == 1 else 0)
        min_swaps = min(min_swaps, total_number_of_1s - total_number_of_1s_currently)

    return min_swaps


def First_Negative(numbers: list[int], k: int) -> list[int]:
    # O(n) time and O(k) space
    #

    n = len(numbers)
    res = []
    dq = deque()

    for i in range(k):
        if numbers[i] < 0: dq.append(i)

    for i in range(k, n):
        res.append(numbers[dq[0]]) if dq else res.append(0)

        while dq and dq[0] < i - k + 1: dq.popleft()
        if numbers[i] < 0: dq.append(i)

    if dq: res.append(numbers[dq[0]])
    else: res.append(0)

    return res

def Chocolate_Distribution(numbers: list[int], k: int) -> int:
    numbers.sort()
    n = len(numbers)

    min_diff = sys.maxsize
    for i in range(n - k + 1):
        min_diff = min(min_diff, numbers[i + k - 1] - numbers[i])

    return min_diff

arr = [7, 3, 2, 4, 9, 12, 56]
m = 3
print(Chocolate_Distribution(arr, m))
