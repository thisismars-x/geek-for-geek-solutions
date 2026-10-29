# miscellaneous practices
#

# rotate a matrix
#

from typing import Sequence

def Rotate_Matrix(matrix: list[list]) -> list[list]:
    matrix_new = []

    r, c = len(matrix), len(matrix[0])

    for j in range(c):
        tmp_row = []
        for i in range(r - 1, -1, -1):
            tmp_row.append(matrix[i][j])

        matrix_new.append(tmp_row)

    return matrix_new

def Print_Matrix(matrix: list[list]):
    r, c = len(matrix), len(matrix[0])

    print("[")
    for i in range(r):
        print("\t[", end='\t')
        for j in range(c):
            print(matrix[i][j], end='\t')
        print("]")
    print("]")

def Number_Of_Occurence(numbers: list[int], k: int) -> int:
    n = len(numbers)

    lo, hi = 0, n - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if numbers[mid] >= k:
            hi = mid - 1
        else: lo = mid + 1

    lower_bound = lo

    lo, hi = 0, n - 1
    while lo <= hi:
        mid = (lo + hi) // 2

        if numbers[mid] <= k:
            lo = mid + 1
        else:
            hi = mid - 1

    higher_bound = hi

    return higher_bound - lower_bound + 1


def Binary_Search(numbers: list[int], target: int) -> int | None:
    lo, hi = 0, len(numbers) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if numbers[mid] == target: return mid

        if numbers[mid] > target: hi = mid - 1
        else: lo = mid + 1

def Subset_Generation(some: Sequence) -> list[list[int]]:
    n = len(some)
    result = []

    for i in range(1 << n):
        tmp_subset = []
        for j in range(n):
            if i & (1 << j): tmp_subset.append(some[j])
        result.append(tmp_subset)

    return result
