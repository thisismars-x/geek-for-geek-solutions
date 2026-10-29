# Searching
import sys
from operator import xor
from functools import reduce, partial

def Find_Second_Largest(numbers: list[int]) -> int:
    if (size := len(numbers)) < 2: raise RuntimeError(f"Can not call Find_Second_Largest, on list with size {size}")
    # naive solution
    # largest = -sys.maxsize
    # for number in numbers: largest = max(largest, number)

    # second_largest = -sys.maxsize
    # for number in numbers:
    #     if second_largest < number < largest:
    #         second_largest = number

    # return second_largest

    # single pass solution
    second_largest, largest = -sys.maxsize, -sys.maxsize
    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number

    return second_largest

def Local_Min_Max(numbers: list[int]) -> list[int]:
    result = [numbers[0]]

    for i in range(1, len(numbers) - 1):
        ## check for local minima and maxima
        if numbers[i] > result[-1] and numbers[i] > numbers[i + 1]: result.append(numbers[i])
        elif numbers[i] < result[-1] and numbers[i] < numbers[i + 1]: result.append(numbers[i])

    if result[-1] != numbers[-1]: result.append(numbers[-1])

    return result

def Insertion_Position(numbers: list[int], number: int) -> int:
    lo, hi = 0, len(numbers) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if numbers[mid] == number: return mid
        if numbers[mid] > number: hi = mid - 1
        else: lo = mid + 1

    return lo

def Lower_Bound(numbers: list[int], number: int) -> int:

    lo, hi = 0, len(numbers) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if numbers[mid] >= number: hi = mid - 1
        else: lo = mid + 1

    return lo

def Upper_Bound(numbers: list[int], number: int) -> int:
    lo, hi = 0, len(numbers) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if numbers[mid] <= number: lo = mid + 1
        else: hi = mid - 1

    return lo

Single_Element = partial(reduce, xor)

def Missing_Natural(numbers: list[int]) -> int:
    if numbers[0] != 1: return 1
    # This supposes numbers start from 1
    # naive fast approach
    # n = len(numbers) + 1
    # return n * (n + 1) // 2 - sum(numbers)

    # Binary search approach FASTER
    n = len(numbers)
    lo, hi = 0, n - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if numbers[mid] == mid + 1 or numbers[mid] < mid + 1:
            # everything is good
            lo = mid + 1

        else: hi = mid - 1

    return lo + 1

    # Naive search
    #

    # n = len(numbers)
    # for i in range(n - 1):
    #     if numbers[i + 1] == 1 + numbers[i]: continue
    #     return 1 + numbers[i] # this will happen by design

def Number_Of_Occurence(numbers: list[int], number: int) -> int:
    n = len(numbers)
    lo, hi = 0, n - 1

    while lo <= hi: # find lower bound
        mid = (lo + hi) // 2
        if numbers[mid] >= number: hi = mid - 1
        else: lo = mid + 1

    lower_bound = lo

    lo, hi = 0, n - 1
    while lo <= hi: # find upper bound
        mid = (lo + hi) // 2
        if numbers[mid] <= number: lo = mid + 1
        else: hi = mid - 1

    upper_bound = lo

    return upper_bound - lower_bound

def Search_Rotated_Array(numbers: list[int], number: int) -> int:
    n = len(numbers)
    lo, hi = 0, n - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if numbers[lo] <= numbers[hi]: break

        if numbers[mid] > numbers[hi]: lo = mid + 1
        else: hi = mid

    l1, l2 = Lower_Bound(numbers[:lo], number), Lower_Bound(numbers[lo:], number)
    if numbers[l1] != number: l1 = 0
    if numbers[l2 + lo] != number: l2 = 0
    if l1: return l1
    if l2: return l2 + lo
    return -1


def Closest_K_Elems(nums: list[int], k: int, x: int) -> list[int]:
    n = len(nums)
    res = []

    pos = Lower_Bound(nums, x)
    left, right = pos - 1, pos + 1 if nums[pos] == x else pos

    while len(res) < k:
        if left < 0: left = right
        if right > n: right = left

        left_diff = abs(nums[left] - x)
        right_diff = abs(x - nums[right])

        if left_diff < right_diff:
            res.append(nums[left])
            left -= 1
        else:
            res.append(nums[right])
            right += 1

    return res


def Search_Almost_Sorted(nums: list[int], k: int) -> int:
    n = len(nums)
    lo, hi = 0, n - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == k: return mid
        if mid > 0 and nums[mid - 1] == k: return mid - 1
        if mid < n - 1 and nums[mid + 1] == k: return mid + 1

        if nums[mid] > k: hi = mid - 2
        else: lo = mid + 2

    return -1

def Find_Peak_Elem(nums: list[int]) -> int:
    lo, hi = 1, len(nums) - 1 - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid - 1] < nums[mid] < nums[mid + 1]: return mid
        if nums[mid] > nums[mid + 1]: lo = mid + 1
        else: hi = mid - 1

    return hi
