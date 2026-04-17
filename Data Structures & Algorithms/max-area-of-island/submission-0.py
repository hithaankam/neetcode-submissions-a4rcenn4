class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_area = 0
        def bfs(i, j):
            queue = deque([])
            queue.append((i, j))
            visited = set()
            area = 0
            visited.add((i, j))
            while queue:
                r, c = queue.popleft()
                area += 1
                for dx, dy in directions:
                    nx, ny = dx + r, dy + c
                    if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                #print(queue)
            return area
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                        max_area = max(max_area, bfs(i, j))

        return max_area
