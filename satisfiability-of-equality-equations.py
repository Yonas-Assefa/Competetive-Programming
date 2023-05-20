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
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    def pr(self):
        print(self.parent)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        n = len(equations)

        for i in range(n):
            eq = equations[i]
            if eq[1] == "=":
                char1 = ord(eq[0]) - 97
                char2 = ord(eq[3]) - 97
                uf.union(char1, char2)
        # uf.pr()
        for j in range(n):
            eq = equations[j]
            if eq[1] == "!":
                char1 = ord(eq[0]) - 97
                char2 = ord(eq[3]) - 97

                # print(uf.find(char1))
                # print(uf.find(char2))
                if uf.connected(char1, char2):
                    return False
        
        return True