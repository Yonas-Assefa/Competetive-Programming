class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.adjList = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    self.adjList[i].append(j)
        self.visited = set()
        count = 0
        for i in self.adjList:
            if i not in self.visited:
                count += 1
                self.dfs(i)
        return count
    def dfs(self, vertex):
        
        self.visited.add(vertex)

        for neighbour in self.adjList[vertex]:
            if neighbour not in self.visited:
                self.dfs(neighbour)