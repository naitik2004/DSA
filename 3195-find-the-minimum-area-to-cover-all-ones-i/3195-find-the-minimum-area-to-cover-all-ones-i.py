# class Solution(object):
#     def minimumArea(self, grid):
#         a_min, a_max = float('inf'), float('-inf')  
#         b_min, b_max = float('inf'), float('-inf')  
#         for i in range(len(grid)):
#             for j in range(len(grid)):
#                 if grid[i][j] == 1:
#                     a_min = min(a_min, i)
#                     a_max = max(a_max, i)
#                     b_min = min(b_min, j)
#                     b_max = max(b_max, j)

#         if a_min == float("inf"):
#             return 0

#         return (a_max - a_min + 1) * (b_max - b_min + 1)


class Solution(object):
    def minimumArea(self, grid):
        a_min, a_max = len(grid), -1
        b_min, b_max = len(grid[0]), -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    a_min = min(a_min, i)
                    a_max = max(a_max, i)
                    b_min = min(b_min, j)
                    b_max = max(b_max, j)

        if a_max == -1:
            return 0

        return (a_max - a_min + 1) * (b_max - b_min + 1)

        
        