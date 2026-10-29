from reprlib import repr
from sys import maxsize

def Triple_Sum(numbers: list[int], target: int) -> tuple[int, int, int]:
    # if target sum is not found, raise ValueError

    numbers.sort()
    n = len(numbers)

    for i in range(n - 1):
        l = i + 1
        r = n - 1

        required_sum = target - numbers[i]

        while l <= r:
            if required_sum == (s := numbers[l] + numbers[r]): return numbers[i], numbers[l], numbers[r]
            if s > required_sum: r -= 1
            else: l += 1

    raise ValueError(f"Can not find target sum = {target} in list = {repr(numbers)}")


    # naive solution
    # O(n^3)

    # n = len(numbers)

    # for i in range(n):
    #     for j in range(n):
    #         for k in range(n):
    #             if numbers[i] + numbers[j] + numbers[k] == target and i != j != k: return numbers[i], numbers[j], numbers[k]

    # raise ValueError(f"Can not find target sum = {target} in list = {repr(numbers)}")


def Closest_Pairs(numbers_A: list[int], numbers_B: list[int], target: int) -> tuple[int, int]:
    # we can go O(n)

    n = len(numbers_A)
    l, r = 0, n - 1

    min_diff = maxsize

    while l <= r:
        s = numbers_A[l] + numbers_B[r]
        curr_diff = abs(s - target)

        if curr_diff < min_diff:
            min_diff = curr_diff
            result = [numbers_A[l], numbers_B[r]]

        if s > target: r -= 1
        else: l += 1

    return tuple(result) # type: ignore RESULT WILL NEVER BE UNBOUND BECAUSE THE NUMBERS IN THE LIST WILL ALWAYS ADD TO LESS THAN `maxsize`


    # naive solution
    # at least O(n^2)
    #

    # n = len(numbers_A)
    # min_diff = maxsize

    # result = [0, 0]

    # for i in range(n):
    #     for j in range(n):
    #         s = numbers_A[i] + numbers_B[j]
    #         curr_diff = abs(s - target)

    #         if curr_diff < min_diff:
    #             min_diff = curr_diff
    #             result = [numbers_A[i], numbers_B[j]]


    # return result[0], result[1]


def Container_Most_Water(numbers: list[int]) -> int:
    n = len(numbers)

    l, r = 0, n - 1
    water = -maxsize

    while l <= r:
        curr_water = min(numbers[l], numbers[r]) * (r - l)
        water = max(water, curr_water)

        if numbers[l] < numbers[r]: l += 1
        else: r -= 1

    return water


def Common_In_Three_Sorted_Arrays(numbers_A: list[int], numbers_B: list[int], numbers_C: list[int]) -> list[int]:
    res: list[int] = []

    n1, n2, n3 = len(numbers_A), len(numbers_B), len(numbers_C)
    i, j, k = 0, 0, 0

    while i < n1 and j < n2 and k < n3:
        if numbers_A[i] == numbers_B[j] == numbers_C[k]:
            if len(res) > 0 and res[-1] == numbers_A[i]: continue # in case of duplicate value skip
            else: res.append(numbers_A[i])

            i += 1
            j += 1
            k += 1

        elif numbers_A[i] < numbers_B[j] and numbers_A[j] < numbers_C[k]: i += 1
        elif numbers_B[j] < numbers_A[i] and numbers_B[j] < numbers_C[k]: j += 1
        else: k += 1

    return res

def Reverse_Words(string: str) -> str:

    res = []

    n = len(string)
    l, r = n-1, n-1

    while 0 < l <= r:
        if string[l] == ".":
            if l == r: # skip .
                l -= 1
                r -= 1
                continue
            string_ = string[l + 1: r + 1]
            res.append(string_)
            r = l
        else: l -= 1

        if l == 0 and string[l] != ".": res.append(string[l: r + 1])

    return ".".join(filter(lambda x: len(x) > 0, res))

def Catch_Thieves(arr: list[int], k: int) -> int:
    res = 0
    n = len(arr)

    police, thief = 0, 0

    while police < n and thief < n:

        while police < n and arr[police] == 'T': police += 1
        while thief < n and arr[thief] == 'P': thief += 1

        if police < n and thief < n and abs(police - thief) <= k:
            res += 1
            police += 1
            thief += 1

        elif police < thief: police += 1
        else: thief += 1

    return res
