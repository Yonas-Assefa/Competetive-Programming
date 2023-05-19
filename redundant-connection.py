class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        ans = None
        for u, v in edges:
            if not uf.union(u - 1, v - 1):
                ans = [u, v]
            
        
        return ans












# def findRedundantConnection(edges):
#     n = len(edges)
#     uf = UnionFind(n)

#     for edge in reversed(edges):
#         if not uf.union(edge[0] - 1, edge[1] - 1):
#             return edge

#     return None