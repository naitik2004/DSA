class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        for i in range(m):
            if grid[i][0] == 1:
                queue.append((i,0))
                grid[i][0] = 0
            if grid[i][n-1] == 1:
                queue.append((i,n-1))
                grid[i][n-1] = 0

        for j in range(n):
            if grid[0][j] == 1:
                queue.append((0,j))
                grid[0][j] = 0
            if grid[m-1][j] == 1:
                queue.append((m-1,j))
                grid[m-1][j] = 0

        while queue:
            x, y = queue.popleft()
            for a,b in dir:
                xx,yy = x+a, y+b
                if xx < m and yy < n and xx >= 0 and yy >= 0 and grid[xx][yy] == 1:
                    queue.append((xx,yy))
                    grid[xx][yy] = 0

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res +=1

        return res





