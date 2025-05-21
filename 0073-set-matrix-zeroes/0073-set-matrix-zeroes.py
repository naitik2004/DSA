class Solution(object):
    def setZeroes(self, matrix):
        row = []
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)

        for i in range(len(col)):
            for j in range(len(matrix)):
                matrix[j][col[i]] = 0
                matrix[row[i]][j] = 0
        return(matrix)



