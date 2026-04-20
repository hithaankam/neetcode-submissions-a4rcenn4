class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for u, v in prerequisites:
            indegree[u] += 1
            adj[v].append(u)
        queue = deque([])
        visited = set()
        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)
                visited.add(c)
        ans = []
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for nei in adj[curr]:
                if nei not in visited:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
                        visited.add(nei)
        if len(ans) != numCourses:
            return []
        return ans