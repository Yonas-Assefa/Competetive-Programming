class Disjoint:
    def __init__(self, size):
        self.rep = [ i for i in range(size)]
        self.rank = [ 1 for i in range(size)]

    def find(self, x):
        if x == self.rep[x]:
            return x
        
        the_rep = self.find(self.rep[x])
        self.rep[x] = the_rep

        return the_rep

    def union(self, x, y):

        repx = self.find(x)
        repy = self.find(y)

        rankx = self.rank[repx]
        ranky = self.rank[repy]
        
        if repx != repy:

            if rankx < ranky:
                self.rep[repx] = repy
                self.rank[repy] = max(ranky, 1 + rankx)
            
            else:
                self.rep[repy] = repx
                self.rank[repx] = max(rankx, 1 + ranky)
            
    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        union_find = Disjoint(n)

        for n1, n2 in edges:
            union_find.union(n1, n2)
        
        return union_find.connected(source, destination)






























    #     self.adjList = defaultdict(list)
    #     for edge in edges:
    #         self.adjList[edge[0]].append(edge[1])
    #         self.adjList[edge[1]].append(edge[0])
        
    #     self.visited = set()
    #     self.dest = destination
    #     print(self.adjList)
    #     self.ans = False
    #     return self.dfs(source)

    # def dfs(self, curNode):
    #     # print(curNode)
            
    #     if curNode == self.dest:
    #         return True
            
    #     if curNode not in self.visited:
    #         self.visited.add(curNode)

    #         for child in self.adjList[curNode]:
    #             if self.dfs(child):
    #                 return True
    #     return False