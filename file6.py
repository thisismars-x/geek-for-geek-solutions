# sliding window
#

from collections import defaultdict

def Smallest_Window(numbers: str) -> int:
    # returns the smallest window containing 0, 1, 2
    #
    # This below does not care about the window size, but works O(n)
    # n = len(numbers)
    # start, end = 0, 0

    # # found_0, found_1, found_2
    # found = [False, False, False]

    # while end < n:
    #     if numbers[end] in ('0', '1', '2'): found[ord(numbers[end]) - ord('0')] = True
    #     if all(found): return end - start + 1
    #     end += 1

    # This solution is O(n) as well, but gives the smallest possible window

    n = len(numbers)
    start, end = 0, 0

    # Stores frequency of 0, 1, 2 in this window
    found = [0, 0, 0]

    min_window_len = n

    while end < n:
        if numbers[end] in ('0', '1', '2'): found[ord(numbers[end]) - ord('0')] += 1
        if all((x > 0 for x in found)):
            ##### we have to trim the window here
            curr_window_len = end - start + 1
            while found[ (index := ord(numbers[start]) - ord('0')) ] > 1:
                found[index] -= 1
                curr_window_len -= 1
                start += 1

            min_window_len = min(min_window_len, curr_window_len)
        end += 1

    return min_window_len if all((x > 0 for x in found)) else -1


def Subarrays_With_Prod_Less_Than_K(numbers: list[int], k: int) -> int:
    n = len(numbers)
    start, end = 0, 0
    n_subarrays = 0

    curr_prod = 1
    while end < n:
        curr_prod *= numbers[end]

        while curr_prod >= k:
            curr_prod //= numbers[start]
            start += 1

        n_subarrays += (end - start + 1)
        end += 1

    return n_subarrays


def Count_Susbtring_With_All_Vowels(string: str) -> int:
    # returns number of valid substrings
    #
    n = len(string)

    n_substrings = 0
    vowels = "aeiou"

    freq = {k: 0 for k in vowels}
    start, end = 0, 0

    redun_vowels = 0
    while end < n:
        curr_char = string[end]

        if curr_char in vowels:
            freq[curr_char] += 1
            while freq.get(string[start], 0) > 1:
                freq[string[start]] -= 1
                start += 1
                redun_vowels += 1

            if all(freq.values()): n_substrings += 1 + redun_vowels
        else:
            freq = {k: 0 for k in vowels}
            redun_vowels = 0
            start = end + 1
        end += 1

    return n_substrings

def Subarray_With_Sum_Lt_Target(numbers: list[int], target: int) -> int:
    n = len(numbers)
    n_subarrays = 0

    start, end = 0, 0

    curr_sum = 0

    while end < n:
        curr_sum += numbers[end]

        while curr_sum >= target:
            curr_sum -= numbers[start]
            start += 1

        n_subarrays += (end-start+1)
        end += 1

    return n_subarrays

def Subarray_With_K_Equal_Pairs(numbers: list[int], k: int) -> int:
    n = len(numbers)
    res = 0

    start, end = 0, 0
    table = defaultdict(int)

    curr_npairs = 0

    while end < n:
        curr_npairs += table[numbers[end]]
        table[numbers[end]] += 1

        while curr_npairs >= k:
            res += (n - end)
            table[numbers[start]] -= 1
            curr_npairs -= table[numbers[start]]
            start += 1

        end += 1


    return res


arr = [ 2, 1, 4, 2, 5, 2 , 6, 2, 6]
print(Subarray_With_K_Equal_Pairs(arr, 3))
