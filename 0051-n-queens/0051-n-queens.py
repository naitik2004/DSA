class Solution(object):
    def isSafe(self, board, row, col, n):
        for j in range(n):
            if board[row][j] == "Q":
                return False

        for i in range(n):
            if board[i][col] == 'Q':
                return False

        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def nQueens(self, board, row, n, ans):
        if row == n:
            ans.append(["".join(i) for i in board])
            return 

        for j in range(n):
            if self.isSafe(board, row, j, n):
                board[row][j] = "Q"
                self.nQueens(board, row+1, n, ans)
                board[row][j] = "."
                

    def solveNQueens(self, n):
        board = [["."] * n for _ in range(n)]
        ans = []
        self.nQueens(board, 0, n, ans)
        return ans
