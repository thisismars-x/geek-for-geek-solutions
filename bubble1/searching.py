
from sys import maxsize

class ImpossibleError(Exception): ...

def Second_Largest(nums: list[int]) -> int:
    largest = second_largest = -maxsize

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num

    return second_largest

def Local_Min_Max(nums: list[int]) -> list[int]:
    res = [ nums[0] ]

    # first remove the flat lines
    # This is still O(n)
    #
    # i = 1
    # while True:
    #     if i > len(nums) - 1: break
    #     curr, before = nums[i], nums[i - 1]
    #     if curr == before:
    #         del nums[i]
    #     else:
    #         i += 1


    # saving the last unique number for flat lines
    last_num = nums[0]
    for i in range(1, len(nums) - 1):
        before, curr, after = nums[i - 1], nums[i], nums[i + 1]

        if curr == after: continue
        if curr == before: before = last_num
        if curr != last_num: last_num = curr

        # is this local minima
        if curr < before and curr < after: res.append(curr)

        # is this local maxima
        if curr > before and curr > after: res.append(curr)


    if res[-1] != nums[-1]: res.append(nums[-1])

    return res

# Binary search
#

def Insertion_Pos(nums: list[int], k: int) -> int:
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == k: return mid

        if nums[mid] > k: hi = mid - 1
        else: lo = mid + 1

    return lo

    # lo, hi = 0, len(nums)

    # while lo < hi:
    #     mid = (lo + hi) // 2
    #     if nums[mid] == k: return mid

    #     if nums[mid] > k: hi = mid
    #     else: lo = mid + 1

    # return lo

def Lower_Bound(nums: list[int], k: int) -> int:
    # given a bunch of nums what is the lowest pos, you can insert k into
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] >= k:
            hi = mid - 1
        else: lo = mid + 1

    return lo

def Upper_Bound(nums: list[int], k: int) -> int:
    # given a bunch of nums what is the lowest pos, you can insert k into
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] <= k: lo = mid + 1
        else: hi = mid - 1

    return lo

def Elem_Less_Than_Three_Times(nums: list[int]) -> int:
    # my twist on the question single elem in sorted array
    #
    # a = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4]
    #
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid -= mid % 3

        if mid + 2 > len(nums) - 1: return nums[mid]
        if nums[mid] == nums[mid + 1] == nums[mid + 2]:
            lo = mid + 3

        else:
            hi = mid - 1

    return nums[lo]

# from time import perf_counter

# make_list_start = perf_counter()
# nums = list(range(99999999))
# nums.remove(99999999 - 21478)
# time_to_make_list = perf_counter() - make_list_start
# print(f"Skipping the number = {99999999 - 21478}, time_to_make_list = {time_to_make_list} seconds.")

def Linear_Search(nums: list[int]) -> int:
    # find the missing number from 0..
    for i in range(len(nums)):
        if i != nums[i]:
            return i

    raise ImpossibleError


def Binary_Search(nums: list[int]) -> int:
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == mid:
            lo = mid + 1
        elif nums[mid] > mid: hi = mid - 1
        else: lo = mid + 1

    return nums[lo] - 1

# time_to_bin_search_start = perf_counter()
# num_missing = Binary_Search(nums)
# time_to_bin_search = perf_counter() - time_to_bin_search_start
# print(f"Number missing  = {num_missing}, time_taken = {time_to_bin_search} seconds :: USING BINARY SEARCH")

# time_to_linear_search_start = perf_counter()
# num_missing = Linear_Search(nums)
# time_to_linear_search = perf_counter() - time_to_bin_search_start
# print(f"Number missing  = {num_missing}, time_taken = {time_to_linear_search} seconds :: USING LINEAR SEARCH")

# print(f"Speedup using Binary_Search over Linear_Search = {int(time_to_linear_search / time_to_bin_search)}x.")


def Search_In_Matrix(mat: list[list[int]], k: int) -> bool:
    r, c = len(mat), len(mat[0])
    lo, hi = 0, r*c - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        row = mid // c
        col = mid - (row * c)
        if mat[row][col] == k: return True
        if mat[row][col] > k: hi = mid - 1
        else: lo = mid + 1

    return False

def Search_In_Rotated_Arr(nums: list[int], k: int) -> int:

    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[lo] <= nums[mid] <= nums[hi]: break

        if nums[lo] > nums[mid]: hi= mid
        else: lo = mid + 1

    insert_pos_1, insert_pos_2 = Insertion_Pos(nums[:lo], k), Insertion_Pos(nums[lo:], k)
    if insert_pos_1 < lo and nums[insert_pos_1] == k: return insert_pos_1
    if insert_pos_2 < len(nums) - lo and nums[insert_pos_2 + lo] == k: return insert_pos_2 + lo

    return -1


def Search_Almost_Sorted(nums: list[int], k: int) -> int:

    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == k: return mid
        if mid - 1 > -1 and nums[mid - 1] == k: return mid - 1
        if mid + 1 < len(nums) and nums[mid + 1] == k: return mid + 1

        if nums[mid] > k: hi = mid - 2
        else: lo = mid + 2

    return -1
