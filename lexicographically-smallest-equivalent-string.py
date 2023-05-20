class UnionFind:
    def __init__(self):
        self.parent = {i : i for i in range(26)}
        self.rank = [i for i in range(26)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
    def pr(self):
        print(self.parent)



class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        len1 = len(s1)
        for i in range(len1):
            char1 = ord(s1[i]) - 97
            char2 = ord(s2[i]) - 97
            print(uf.find(char1), uf.find(char2))
            uf.union(char1, char2)
            uf.pr()
        
        len2 = len(baseStr)
        ans = ""
        for i in range(len2):
            char = ord(baseStr[i]) - 97
            val = uf.find(char)
            charVal = chr(val + 97)
            ans += (charVal)
        return ans