class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # n = len(matrix)

        # for i in range(n):
        #     for j in range(i, n):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # for row in matrix:
        #     row.reverse()

        n = len(matrix)
        result = [[0] * n for _ in range(n)] 

        for i in range(n):
            for j in range(n):
                result[j][n - 1 - i] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = result[i][j]