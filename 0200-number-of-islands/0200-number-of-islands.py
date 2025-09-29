class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        island = 0
        queue = deque()
        visited = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i,j) not in visited:

                    island += 1

                    queue.append((i,j))
                    visited.add((i,j))

                while queue:
                    x ,y  = queue.popleft()
                    for dx, dy in dir:
                        xx = dx + x
                        yy = dy + y
                        if 0 <= xx < n and 0 <= yy < m and (xx,yy) not in visited and grid[xx][yy] == '1':
                            queue.append((xx,yy))
                            visited.add((xx,yy))

        return island