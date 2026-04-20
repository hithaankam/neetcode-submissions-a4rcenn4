class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c):
            if board[r][c] == 'O':
                board[r][c] = 'S'
            visited.add((r, c))
            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and board[nx][ny] != 'X':
                    print((r, c), (nx, ny))
                    dfs(nx, ny)
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == n - 1 or j == m - 1):
                    board[i][j] = 'S'
                    dfs(i, j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
