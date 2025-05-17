class Solution(object):
    def isSafe(self,board, row, col,dig):
        #horizontal
        for j in range(9):
            if board[row][j] == str(dig):
                return False

        #vertical
        for i in range(9):
            if board[i][col] == str(dig):
                return False
        
        #in Grids
        srow = (row//3)*3
        scol = (col//3)*3
        for i in range(srow, srow+3):
            for j in range(scol, scol+3):
                if board[i][j] == str(dig):
                    return False
        
        return True

    def helper(self,board, row, col):
        if row == 9:
            return True
        
        nrow = row
        ncol = col + 1
        if ncol == 9:
            ncol = 0
            nrow = row + 1

        if board[row][col] != '.':
            return self.helper(board,nrow,ncol)

        for dig in map(chr, range(ord('1'), ord('9') + 1)):
            if self.isSafe(board, row, col, dig):
                board[row][col] = dig
                if self.helper(board,nrow,ncol):
                    return True
                board[row][col] = '.'
        
        return False


    def solveSudoku(self, board):
        self.helper(board, 0 ,0)


# class Solution(object):
#     def isSafe(self, board, row, col, dig):
#         # horizontal
#         for j in range(9):
#             if board[row][j] == str(dig):
#                 return False

#         # vertical
#         for i in range(9):
#             if board[i][col] == str(dig):
#                 return False

#         # in Grids
#         srow = (row // 3) * 3
#         scol = (col // 3) * 3  # \U0001f6e0 fixed: was wrongly reassigning srow
#         for i in range(srow, srow + 3):
#             for j in range(scol, scol + 3):
#                 if board[i][j] == str(dig):
#                     return False

#         return True

#     def helper(self, board, row, col):
#         if row == 9:
#             return True

#         nrow = row
#         ncol = col + 1
#         if ncol == 9:  #  fixed: it should be 9, not 0
#             ncol = 0
#             nrow = row + 1

#         if board[row][col] != '.':
#             return self.helper(board, nrow, ncol)  #  fixed: return added

#         for dig in map(chr, range(ord('1'), ord('9') + 1)):
#             if self.isSafe(board, row, col, dig):  #  fixed: added self
#                 board[row][col] = dig
#                 if self.helper(board, nrow, ncol):  #  fixed: added self
#                     return True
#                 board[row][col] = '.'

#         return False

#     def solveSudoku(self, board):
#         self.helper(board, 0, 0)  #  fixed: added self
