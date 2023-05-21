class UnionFind:
    def __init__(self, n):
        self.parent = {i : i for i in range(n)}
        self.rank = [0 for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.rank[rootY] += 1

            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

        # if repx != repy:

        #     if rankx < ranky:
        #         self.rep[repx] = repy
        #         self.rank[repy] = max(ranky, 1 + rankx)
            
        #     else:
        #         self.rep[repy] = repx
        #         self.rank[repx] = max(rankx, 1 + ranky)

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def count(self):
        comp = 0
        n = len(self.parent)
        for i in range(n):
            if self.find(i) == i:
                comp += 1
        return (n - comp)
    def pr(self):
        print(self.parent)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)
                    # print(i, j)
                    # uf.pr()
        
        maxStones = uf.count()
        return maxStones