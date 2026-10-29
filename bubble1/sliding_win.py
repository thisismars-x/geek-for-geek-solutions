
from sys import maxsize

def Max_Sum_Subarray(nums: list[int], k: int) -> int:
    max_sum = curr_sum = sum(nums[:k])

    for i in range(1, len(nums) - k + 1):
        curr_sum = curr_sum - nums[i - 1] + nums[i + k - 1]
        max_sum = max(curr_sum, max_sum)

    return max_sum


def Count_Distinct(nums: list[int], k: int) -> list[int]:
    count = {}
    for n in nums[:k]: count[n] = count.get(n, 0) + 1

    res = [len(count)]

    for i in range(1, len(nums) - k + 1):
        count[nums[i - 1]] -= 1
        if count[nums[i - 1]] == 0:
            del count[nums[i - 1]]

        count[nums[i + k - 1]] = count.get(nums[i + k - 1], 0) + 1
        res.append(len(count))

    return res

def Max_Mex(nums: list[int], k: int) -> int:
    max_mex = -maxsize

    for i in range(len(nums) - k + 1):
        tmp = nums[i:i+k]
        tmp.sort()

        start = 1
        last_elem_should_not_lead = False
        for number in tmp:
            if number != start:
                max_mex = max(max_mex, start)
                last_elem_should_not_lead = True
                break
            start += 1

        if not last_elem_should_not_lead: max_mex = max(max_mex, start)

    return max_mex

def Min_Swaps(nums: list[int]) -> int:
    count, n = nums.count(1), len(nums)
    if count == 0: return -1

    curr_swaps = min_swaps = nums[:count].count(0)
    for i in range(1, n - count + 1):
        curr_swaps -= not nums[i - 1]
        curr_swaps += not nums[i + count - 1]
        min_swaps = min(min_swaps, curr_swaps)

    return min_swaps

def First_Negative(nums: list[int], k: int) -> list[int]:
    negative = 0
    for n in nums[:k]:
        if n < 0:
            negative = n
            break

    res = [ negative ]

    for i in range(1, len(nums) - k + 1):
        negative = 0
        for n in nums[i:i + k]:
            if n < 0:
                negative = n
                break

        res.append(negative)

    return res


# Variable length window
#

def Max_Consec_Ones(nums: list[int], k: int) -> int:
    start, end, n = 0, 0, len(nums)
    max_len = -maxsize

    curr_n_zeros = 0
    while end < n:
        if nums[end] == 0: curr_n_zeros += 1

        while curr_n_zeros > k:
            curr_n_zeros -= 1 if nums[start] == 0 else 0
            start += 1

        max_len = max(max_len, end - start + 1)
        end += 1

    return max_len


def Subarray_With_Sum(nums: list[int], k: int) -> tuple[int, int] | tuple[int]:
    start, end, n = 0, 0, len(nums)

    curr_sum = 0
    while end < n:
        curr_sum += nums[end]
        print(curr_sum)

        while curr_sum - nums[start] >= k and start < end:
            curr_sum -= nums[start]
            start += 1

        if curr_sum == k:
            return start, end

        end += 1

    return -1,


# Min len window
#

def Smallest_Subarray_With_Gt_Sum(nums: list[int], k: int) -> int:
    start, end, n = 0, 0, len(nums)
    min_len = maxsize

    curr_sum = 0
    while end < n:
        curr_sum += nums[end]

        while curr_sum - nums[start] > k:
            curr_sum -= nums[start]
            start += 1

        if curr_sum > k: min_len = min(min_len, end - start + 1)
        end += 1

    return min_len if min_len != maxsize else 0

def Min_Win_Subseq(s1: str, s2: str) -> str:
    n = len(s1)
    count = {k: 0 for k in s2}

    min_len = maxsize
    start, end = 0, 0
    min_start, min_end = 0, 0

    while end < n:
        if s1[end] in count:
            count[s1[end]] += 1

        # if all values are present we can shrink the window
        while all(count.values()) and count.get(s1[start], 2) > 1:
            if s1[start] in count: count[s1[start]] -= 1
            start += 1

        if all(count.values()):
            curr_len = end - start + 1
            if curr_len < min_len:
                min_len = curr_len
                min_start, min_end = start, end

        end += 1

    return s1[min_start: min_end + 1]


def Smallest_Containing_012(nums: list[int]) -> int:
    min_len, start, end, n = maxsize, 0, 0, len(nums)

    found = {k:0 for k in (0, 1, 2)}
    while end < n:
        found[nums[end]] += 1

        while all(found.values()) and found[nums[start]] > 2:
            found[nums[start]] -= 1
            start += 1

        if all(found.values()): min_len = min(min_len, end - start + 1)

        end += 1

    return min_len if min_len != maxsize else -1
