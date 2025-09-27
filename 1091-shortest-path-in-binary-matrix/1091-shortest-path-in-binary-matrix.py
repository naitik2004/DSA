class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] != 0 or grid[n-1][m-1] != 0:
            return -1

        visited = [[False]*n for _ in range(n)]

        dir = [(1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)]

        queue = deque()

        queue.append((0,0,1))
        visited[0][0] = True

        while queue:
            x, y , idx = queue.popleft()
            
            if x == m-1 and y == n-1:
                return idx

            for dx, dy in dir:
                xx = dx + x
                yy = dy + y
                if 0 <= xx < m and 0 <= yy < n and not visited[xx][yy] and grid[xx][yy] == 0:
                    visited[xx][yy] = True
                    queue.append((xx, yy, idx + 1))




































































        # visited = [[0 for _ in range(n)] for _ in range(n)]
        # print(visited)
        # count = 0
        # def check(i, j, count): 
        #     count += 1
        #     visited[i][j] = 1

        #     # diagonal DR
        #     if i + 1 < n and j + 1 < n and not vis[i + 1][j + 1] and a[i + 1][j + 1] == 0:
        #         check(i+1, j+1, count)

        #     # down 
        #     if i+1 > m and not visited[i+1][j] and grid[i+1][j] == 0:
        #         solve(i+1,j,count)   
               

        #     # left
        #     if j+1 > m and not visited[i][j+1] and grid[i][j+1] == 0:
        #         solve(i,j+1,solve)

        #     # 
           

        #     if j + 1 < n and not vis[i][j + 1] and a[i][j + 1] == 0:
        #         check(i, j+1, count)

            

        # if grid[0][0] == 0:
        #     check(0,0,count)
        # else:
        #     return -1
        # return count 