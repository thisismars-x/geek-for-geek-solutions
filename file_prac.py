
from sys import maxsize

def Peak_In_Matrix(mat: list[list[int]]) -> tuple[int, int]:
    n, m = len(mat), len(mat[0])

    # for i in range(n):
    #     for j in range(m):
    #         up = mat[i-1][j] if i > 0 else -maxsize
    #         down  = mat[i+1][j] if i + 1 < n else -maxsize
    #         left = mat[i][j-1] if j > 0 else -maxsize
    #         right = mat[i][j+1] if j + 1 < m else -maxsize

    #         if mat[i][j] >= up and mat[i][j] >= down and mat[i][j] >= left and mat[i][j] >= right:
    #             return i, j

    # raise ValueError

    # optimal solution

    lo, hi = 0, m - 1
    while lo <= hi:
        mid = (lo + hi) // 2

        max_row = 0
        for i in range(n):
            if mat[i][mid] > mat[max_row][mid]:
                max_row = i

        left = mat[max_row][mid - 1] if mid > 0 else -maxsize
        right = mat[max_row][mid + 1] if mid + 1 < m else -maxsize

        if mat[max_row][mid] >= left and mat[max_row][mid] >= right: return max_row, mid

        if right > mat[max_row][mid]: lo = mid + 1
        else: right = mid - 1

    raise ValueError


mat = [
    [10, 20, 15],
    [21, 30, 14],
    [7, 16, 32]
]

mat = [[17, 7],
                            [11, 10]]


print(Peak_In_Matrix(mat))
