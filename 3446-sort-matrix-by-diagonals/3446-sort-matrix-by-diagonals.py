class Solution(object):
    def sortMatrix(self, grid):
        n = len(grid)
        diagonals = {}
        
        for i in range(n):
            for j in range(n):
                key = i - j
                if key not in diagonals:
                    diagonals[key] = []
                diagonals[key].append(grid[i][j])
        
        for key in diagonals:
            diagonals[key].sort(reverse=(key >= 0))
        
        for i in range(n):
            for j in range(n):
                key = i - j
                grid[i][j] = diagonals[key].pop(0)
        
        return(grid)

        