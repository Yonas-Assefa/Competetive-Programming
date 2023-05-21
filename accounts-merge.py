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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        
        accountList = defaultdict(lambda : -1)
        for i in range(n):
            acc = accounts[i]
            acc_num = len(acc)

            for j in range(1, acc_num):
                email = accounts[i][j]
                if accountList[email] == -1:
                    accountList[email] = i
                else:
                    uf.union(accountList[email], i)
        
        merged_acct = defaultdict(set)
        for i in range(n):
            parent_acct = uf.find(i)
            merged_acct[parent_acct].update(accounts[i][1:])
        
        return[([accounts[i][0]] + sorted(merged_acct[i])) for i in merged_acct]