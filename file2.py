# two pointers

from sys import maxsize


def Two_Sum(numbers: list[int], target: int) -> tuple[int, int]:
    n = len(numbers)
    lo, hi = 0, n - 1

    while lo <= hi:
        if (sum_ := numbers[lo] + numbers[hi]) == target: return lo + 1, hi + 1 # 1 based indexing

        if sum_ < target: lo += 1
        else: hi -= 1

    return -1, -1

    # naive approach

    # n = len(numbers)

    # for i in range(n):
    #     for j in range(n):
    #         if numbers[i] + numbers[j] == target and i != j: return i + 1, j + 1

    # return -1, -1

def Smallest_Sub_Array_Sum(numbers: list[int], sum_: int) -> int:
    n = len(numbers)

    min_len = maxsize
    left = 0
    total_sum = 0

    for i in range(n):
        total_sum += numbers[i]

        while total_sum > sum_:
            min_len = min(min_len, i - left + 1)
            total_sum -= numbers[left]
            left += 1

    return min_len if min_len < maxsize else 0

def Sentence_Palindrome(sentence: str) -> bool:
    n = len(sentence)
    left, right = 0, n - 1

    while left <= right:
        if not sentence[left].isalnum():
            left += 1
            continue

        if not sentence[right].isalnum():
            right -= 1
            continue

        if sentence[left].upper() != sentence[right].upper(): return False

        left += 1
        right -= 1

    return True
