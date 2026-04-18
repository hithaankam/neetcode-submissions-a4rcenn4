class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        n, m = len(grid), len(grid[0])
        def bfs(r, c):
            queue = deque([])
            queue.append((r, c, 0))
            visited = set()
            visited.add((r, c))

            while queue:
                r, c, steps = queue.popleft()
                #print(r, c)
                if grid[r][c] == 0:
                    return steps
                for dx, dy in directions:
                    nx, ny = r + dx, c + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != -1 and (nx, ny) not in visited:
                        queue.append((nx, ny, steps + 1))
                        visited.add((nx, ny))
                #print(queue)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i, j)
