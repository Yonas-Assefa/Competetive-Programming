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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        m = len(pairs)
        uf = UnionFind(n)

        for u, v in pairs:
            uf.union(u, v)
        
        charDict = defaultdict(lambda: [])
        for i in range(n):
            parent = uf.find(i)
            heappush(charDict[parent], s[i])

        ans = ""
        for i in range(n):
            parent = uf.find(i)
            ans += heappop(charDict[parent])
        return ans