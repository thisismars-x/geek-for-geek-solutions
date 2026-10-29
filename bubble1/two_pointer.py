
from sys import maxsize

def Two_Sum(nums: list[int], k: int) -> tuple[int, int] | None:
    i, j = 0, len(nums) - 1

    while i < j:
        curr_sum = nums[i] + nums[j]
        if curr_sum == k: return i, j
        if curr_sum > k: j -= 1
        else: i += 1

    return None

def Smallest_Subarray_With_Sum(nums: list[int], k: int) -> int:
    i, j, n = 0, 0, len(nums)

    curr_sum = 0
    min_len = maxsize
    while j < n:
        curr_sum += nums[j]

        while curr_sum - nums[i] > k and i < j:
            curr_sum -= nums[i]
            i += 1

        if curr_sum > k: min_len = min(min_len, j - i + 1)
        j += 1

    return min_len if min_len != maxsize else 0

def Remove_Dup(nums: list[int]) -> list[int]:
    n = len(nums)

    offset_for_i = 0
    for i in range(1, n):
        i -= offset_for_i
        if nums[i] == nums[i - 1]:
            offset_for_i += 1
            del nums[i]

    return nums

def Sentence_Palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1

    while i < j:
        if not s[i].isalpha(): i += 1
        elif not s[j].isalpha(): j -= 1
        else:
            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1

    return True

def Three_Sum(nums: list[int], k: int) -> tuple[int, int, int] | None:
    n = len(nums)

    for i in range(n - 2):
        left, middle, right = i, i + 1, n - 1

        while middle < right:
            curr_sum = nums[left] + nums[middle] + nums[right]
            if curr_sum == k: return left, middle, right

            if curr_sum < k: middle += 1
            else: right -= 1

    return None

def Closest_Pair(nums_1: list[int], nums_2: list[int], k: int) -> tuple[int, int] | None:
    left, right = 0, len(nums_2) - 1

    min_diff = maxsize
    pos_i, pos_j = left, right
    while left < len(nums_1) and right > -1:
        curr_sum = nums_1[left] + nums_2[right]
        curr_diff = abs(curr_sum - k)

        if curr_diff < min_diff:
            min_diff = curr_diff
            pos_i, pos_j = left, right


        if curr_sum > k:
            right -= 1
        else:
            left += 1

    # pos_i into nums_1 and pos_j into nums_2
    return pos_i, pos_j

def Container_With_Most_Water(nums: list[int]) -> int:
    max_water = -maxsize
    left, right = 0, len(nums) - 1

    while left < right:
        curr_water = (right - left) * min(nums[right], nums[left])
        max_water = max(max_water, curr_water)

        if nums[left] < nums[right]: left += 1
        else: right -= 1

    return max_water


def Common_In_Three_Arrays(nums_1: list[int], nums_2: list[int], nums_3: list[int]) -> list[int]:
    res = []

    n1, n2, n3 = len(nums_1), len(nums_2), len(nums_3)
    i1, i2, i3 = 0, 0, 0

    while i1 < n1 and i2 < n2 and i3 < n3:
        if nums_1[i1] == nums_2[i2] == nums_3[i3]:
            res.append(nums_1[i1])
            i1 += 1
            i2 += 1
            i3 += 1
        elif nums_1[i1] < nums_2[i2] and nums_1[i1] < nums_3[i3]: i1 += 1
        elif nums_2[i2] < nums_1[i1] and nums_2[i2] < nums_3[i3]: i2 += 1
        else: i3 += 1

    return res

def Reverse_Words(s: str) -> str:

    res = []

    tmp = []
    for char in s[::-1]:
        if char == ".":
            if tmp: res.append("".join(tmp[::-1]))
            tmp.clear()
        else:
            tmp.append(char)

    if tmp: res.append("".join(tmp[::-1]))
    return ".".join(res)


def Policeman_Catch_Thieves(arr: list[str], k: int) -> int:
    police, thief, n = 0, 0, len(arr)

    res = 0
    while police < n and thief < n:

        while arr[police] != 'P' and police < n - 1:
            police += 1

        if arr[police] != 'P': break

        while arr[thief] != 'T' and thief < n - 1:
            thief += 1

        if arr[thief] != 'T': break

        if abs(police - thief) <= k:
            res += 1
            police += 1
            thief += 1
        elif police > thief: thief += 1
        else: police += 1

    return res

def Four_Sum(nums: list[int], k: int) -> bool:
    nums.sort()

    for i in range(len(nums) - 3):
        required_sum = k - nums[i]
        indices = Three_Sum(nums[i + 1:], required_sum)
        if indices: return True

    return False

def Triplet_Closest_To_Target(nums: list[int], k: int) -> int:
    nums.sort()
    n = len(nums)

    min_diff = maxsize
    sum_of_triplets = 0

    for i in range(n - 2):
        left, middle, right = i, i + 1, n - 1

        while middle < right:
            curr_sum = nums[left] + nums[middle] + nums[right]
            curr_diff = abs(curr_sum - k)
            if curr_diff <= min_diff:
                sum_of_triplets = max(curr_sum, curr_sum if curr_diff < min_diff else sum_of_triplets)
                min_diff = curr_diff

            if curr_sum > k:
                right -= 1
            else:
                middle += 1

    return sum_of_triplets

def Count_Triplets(nums: list[int], k: int) -> int:
    res = 0

    for i in range(len(nums) - 2):
        left, middle, right = i, i + 1, len(nums) - 1

        while middle < right:
            curr_sum = nums[left] + nums[middle] + nums[right]
            if curr_sum == k:
                # the array may have duplicates
                res += 1
                if middle + 1 < right and nums[middle + 1] == nums[middle]:
                    middle += 1
                elif right - 1 > middle and nums[right - 1] == nums[right]:
                    right -= 1
                else:
                    middle += 1
                    right -= 1

            elif curr_sum > k:
                right -= 1
            else:
                middle += 1

    return res
