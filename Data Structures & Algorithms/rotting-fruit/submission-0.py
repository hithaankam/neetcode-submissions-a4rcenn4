class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        n, m = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        visited = set()
        for i in range(n):
            for j in range(m):
                grid[i][j] = -grid[i][j]
                if grid[i][j] == -2:
                    grid[i][j] = -0
                    queue.append((i, j, 0))
                    visited.add((i, j))
        while queue:
            r, c, time = queue.popleft()
            if grid[r][c] == -1:
                grid[r][c] = time
            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != -0 and (nx, ny) not in visited:
                    queue.append((nx, ny, time + 1))
                    visited.add((nx, ny))
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == -1:
                    return -1
                ans = max(ans, grid[i][j])
        return ans