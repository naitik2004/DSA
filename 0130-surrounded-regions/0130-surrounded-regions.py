class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        
        res = set()
        queue = deque()

        for i in range(n):
            if board[i][0] == 'O':
                queue.append((i,0))
                res.add((i,0))
            if board[i][m-1] == 'O':
                queue.append((i, m-1))
                res.add((i, m-1))


        for j in range(m):
            if board[0][j] == 'O':
                queue.append((0,j))
                res.add((0,j))
            
            if board[n-1][j] == 'O':
                queue.append((n-1,j))
                res.add((n-1, j))
        
        while queue:
            x , y = queue.popleft()

            for dx, dy in dir:
                xx = dx+x
                yy = dy+y
                if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 'O' and (xx, yy) not in res:
                    queue.append((xx,yy))
                    res.add((xx,yy))

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i, j) not in res:
                    board[i][j] = 'X'

        print(res)
