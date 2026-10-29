# sliding window
#

from sys import maxsize

def Max_Consecutive1s(numbers: list[int], k: int) -> int:
    n = len(numbers)

    # naive solution
    # count = 0

    # for i in range(n):
    #     n_zeros = 0
    #     for j in range(i, n):
    #         if numbers[j] == 0: n_zeros += 1

    #         if n_zeros <= k: count = max(count, j - i + 1)

    # return count

    start, end = 0, 0
    count = 0

    n_zeros = 0
    while end < n:
        if numbers[end] == 0: n_zeros += 1

        while n_zeros > k:
            if numbers[start] == 0:
                n_zeros -= 1
            start += 1

        count = max(count, end - start + 1)
        end += 1

    return count

def Longest_Equal_Substring(string1: str, string2: str, k: int) -> int:
    #
    # Looks like the solution in the website is wrong
    # The solution assumes the substrings in both strings should begin and end at the same place

    n = len(string1)
    max_length = 0
    start, end = 0, 0

    curr_cost = 0
    while end < n:
        curr_cost += abs(ord(string1[end]) - ord(string2[end]))
        while curr_cost >= k:
            curr_cost -= abs(ord(string1[start]) - ord(string2[start]))
            start += 1

        end += 1
        max_length = max(max_length, end - start + 1)


    return max_length

def Fruit_Into_Baskets(numbers: list[int]) -> int:
    n = len(numbers)

    # this algorithm is O(1) space because at any time unique_fruits can have at most 2 items
    unique_fruits = {}
    start, end = 0, 0
    count = 0

    while end < n:
        unique_fruits[numbers[end]] = unique_fruits.get(numbers[end], 0) + 1

        while len(unique_fruits) > 2:
            unique_fruits[numbers[start]] -= 1
            if unique_fruits[numbers[start]] == 0: del unique_fruits[numbers[start]]
            start += 1

        count = max(count, end - start + 1)
        end += 1

    return count


def Subarray_With_Given_Sum(numbers: list[int], sum_: int) -> tuple[int, int] | Literal[-1]:
    n  = len(numbers)
    start, end = 0, 0

    tmp_sum = 0
    while end < n:
        tmp_sum += numbers[end]

        if tmp_sum == sum_:
            return start + 1, end + 1

        while tmp_sum > sum_:
            tmp_sum -= numbers[start]
            start += 1

        end += 1

    return -1

def Smallest_Subarray_With_Sum(numbers: list[int], sum_: int) -> int:
    # length returned
    #
    final_len = n = len(numbers)

    start, end = 0, 0

    curr_sum = 0
    while end < n:
        curr_sum += numbers[end]

        while curr_sum - numbers[start] > sum_:
            curr_sum -= numbers[start]
            start += 1

            final_len = min(final_len, end - start + 1)

        end += 1

    return ( 0 if sum(numbers) < sum_ else final_len ) if final_len else final_len

    # naive solution
    #

    # n = len(numbers)

    # final_len = n
    # for i in range(n):
    #     for j in range(i, n):
    #         temp_sum = sum(numbers[i:j + 1])
    #         if temp_sum > sum_:
    #            final_len = min(final_len, j - i + 1)
    #            break

    # return final_len if final_len != n else 0 if sum(numbers) < sum_ else n

def Smallest_Window_String(s: str, p: str) -> str:
    ns, np = len(s), len(p)

    char_in_p = {}
    for char in p: char_in_p[char] = char_in_p.get(char, 0) + 1

    char_in_s = {}

    start = 0
    min_len = maxsize
    min_start = 0
    count = 0

    for end in range(ns):
        char = s[end]
        char_in_s[char] = char_in_s.get(char, 0) + 1

        if char in char_in_p and char_in_s[char] <= char_in_p[char]:
            count += 1

        while count == np:
            window_len = end - start + 1

            if window_len < min_len:
                min_len = window_len
                min_start = start

            left_char = s[start]

            if left_char in char_in_p:
                if char_in_s[left_char] <= char_in_p[left_char]:
                    count -= 1

                char_in_s[left_char] -= 1

            start += 1

    return "" if min_len == float("inf") else s[min_start:min_start + min_len]
