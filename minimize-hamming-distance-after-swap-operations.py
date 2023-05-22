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

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)
        swapNum = len(allowedSwaps)
       
        for i in range(swapNum):
            u, v = allowedSwaps[i]
            uf.union(u, v)
        
        swaps = defaultdict(dict)
        for i, val in enumerate(source):
            parent = uf.find(i)
            swaps[parent].setdefault(val, 0)
            swaps[parent][val] += 1

        count = 0
        for i, val in enumerate(target):
            if val in swaps[uf.find(i)]:
                swaps[uf.find(i)][val] -= 1
                if not swaps[uf.find(i)][val]:
                    del swaps[uf.find(i)][val]
            else:
                count += 1

        return count