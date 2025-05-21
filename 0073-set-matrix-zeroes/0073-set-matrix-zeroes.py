class Solution(object):
    def setZeroes(self, matrix):
        row = set()
        col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in col:
                    matrix[i][j] = 0
                    


# class Solution(object):
#     def setZeroes(self, matrix):

#         row = []
#         col = []

#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if matrix[i][j] == 0:
#                     row.append(i)
#                     col.append(j)

#         for r in row:
#             for j in range(len(matrix[0])):  
#                 matrix[r][j] = 0

#         for c in col:
#             for i in range(len(matrix)):
#                 matrix[i][c] = 0

#         return(matrix)


