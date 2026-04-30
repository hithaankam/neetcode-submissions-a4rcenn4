class DSU:
    def __init__(self):
        self.par = [i for i in range(101)]
        self.rank = [1 for i in range(101)]
    def find(self, node):
        if self.par[node] == node:
            return node
        res = self.find(self.par[node])
        self.par[node] = res
        return res
    def union(self, u, v):
        par_u, par_v = self.find(u), self.find(v)
        if self.rank[par_u] > self.rank[par_v]:
            self.rank[par_u] += self.rank[par_v]
            self.par[par_v] = self.par[par_u]
        else:
            self.rank[par_v] += self.rank[par_u]
            self.par[par_u] = self.par[par_v]
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()

        for u, v in edges:
            if dsu.find(u) != dsu.find(v):
                dsu.union(u, v)
            else:
                return [u, v]

        