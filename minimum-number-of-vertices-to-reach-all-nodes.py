class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        self.graph = defaultdict(set)
        self.visited = set()
        self.res = set()

        for i,j in edges:
            self.graph[i].add(j)

        for i in range(n):
            if i not in self.visited:
                self.res.add(i)
                self.dfs(i)
        print(self.graph)
        return self.res
        
    def dfs(self, node):
        self.visited.add(node)
        for child in self.graph[node]:
            if child not in self.visited:
                self.dfs(child)
            elif child in self.res:
                self.res.remove(child)