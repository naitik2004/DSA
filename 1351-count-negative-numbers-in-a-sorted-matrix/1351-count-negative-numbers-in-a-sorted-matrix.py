class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # count = 0
        # for row in grid:
        #     lo,hi = 0, len(row)
        #     while lo < hi :
        #         mid = (lo + hi) //2
        #         if row[mid] < 0:
        #             hi = mid
        #         else:
        #             lo = mid +1
        #     count += len(row) - lo
        # return count
    
    
        
        
        # count = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] < 0:
        #             count += 1
        # return count


        count = 0
        m,n = len(grid), len(grid[0])
        row, col = m - 1, 0
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                count += (n - col)
                row -= 1
            else:
                col += 1
        return count