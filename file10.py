# backtracking
#

def N_Queens(n: int) -> list[list[int]]:
    res = []
    board = [[0] * n for _ in range(n)]

    def is_safe(r: int, c: int) -> bool:
        for i in range(r):
            if board[i][c]: return False
        for i in range(c):
            if board[r][i]: return False

        i, j = r-1, c-1
        while i >= 0 and j >= 0:
            if board[i][j]: return False
            i -= 1
            j -= 1

        i, j = r-1, c+1
        while i >= 0 and j < n:
            if board[i][j]: return False
            i -= 1
            j += 1

        return True

    def place_queen(row: int):

        if row == n:
            ans = []

            for i in range(n):
                for j in range(n):
                    if board[i][j]: ans.append(j + 1)

            res.append(ans)
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1
                place_queen(row + 1)
                board[row][col] = 0

    place_queen(0)
    return res
