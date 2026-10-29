# just practise/practice
#

from collections import Counter

def Toggle_Cases(string: str) -> str:
    string_: list[str] = list(string)
    for i in range(1, len(string_)): string_[i] = string_[i].upper() if string_[i].islower() else string_[i].lower()
    return "".join(string_)


def Check_Subsequence(s1: str, s2: str) -> bool:
    n_s1, n_s2 = len(s1), len(s2)
    i, j = 0, 0

    while i < n_s1 and j < n_s2:
        if s1[i] == s2[j]:
            i += 1
        j += 1

    return i == n_s1

def Majority_Element(numbers: list[int]):
    count = Counter(numbers)
    if (number := count.most_common(1)[-1])[-1] > len(numbers) // 2: return number[0]
    return -1


def Search_In_Rotated_Array(numbers: list[int], k: int) -> int:
    n = len(numbers)

    lo, hi = 0, n - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if numbers[lo] <= numbers[hi]: break # actually we don't even need to know numbers[mid]

        if numbers[hi] < numbers[mid]:
            lo = mid
        else:
            hi = mid - 1

    arr1, arr2 = numbers[:hi + 1], numbers[hi + 1:]
    #
    # first search on arr1
    lo1, hi1 = 0, hi
    while lo1 <= hi1:
        mid = (lo1 + hi1) // 2
        if arr1[mid] == k: return mid
        if arr1[mid] > k: hi1 = mid - 1
        else: lo1 = mid + 1

    lo2, hi2 = 0, (n - hi - 1) - 1
    while lo2 <= hi2:
        mid = (lo2 + hi2) // 2
        if arr2[mid] == k: return hi + 1 + mid
        if arr2[mid] > k: hi2 = mid - 1
        else: lo2 = mid + 1

    return -1

def Check_Palindrom_Binary(number: int) -> bool:
    binary = bin(number)[2:]
    lo, hi = 0, len(binary) - 1

    while lo < hi:
        if binary[lo] != binary[hi]: return False
        lo += 1
        hi -= 1

    return True

def Triplet_Sum(numbers: list[int], k: int) -> bool:
    n = len(numbers)

    numbers.sort()

    for i in range(n - 2):
        left, middle, right = i, i + 1, n - 1

        required_sum = k - numbers[left]

        while middle < right:
            if (s := numbers[middle] + numbers[right]) == required_sum: return True
            if s < required_sum: middle += 1
            else: right -= 1

    return False

def Count_Distinct_In_Every_Window(numbers: list[int], k: int) -> list[int]:
    n = len(numbers)
    res = []

    distinct_in_curr_win = {}
    for num in numbers[:k]: distinct_in_curr_win[num] = distinct_in_curr_win.get(num, 0) + 1
    res.append(len(distinct_in_curr_win))

    for i in range(1, n - k + 1):
        distinct_in_curr_win[numbers[i - 1]] -= 1
        distinct_in_curr_win[numbers[i + k - 1]] = distinct_in_curr_win.get(numbers[i + k - 1], 0) + 1
        if distinct_in_curr_win[numbers[i - 1]] == 0: del distinct_in_curr_win[numbers[i - 1]]
        print(distinct_in_curr_win)
        res.append(len(distinct_in_curr_win))

    return res
