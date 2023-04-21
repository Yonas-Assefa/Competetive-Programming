class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        self.dest = len(graph) - 1
        self.graph = graph
        self.dfs(0, [])
        
        return self.ans
    
    def dfs(self, curNode, res):
        if curNode == self.dest:
            self.ans.append(res + [curNode])
            return

        for child in self.graph[curNode]:
            self.dfs(child, res + [curNode])