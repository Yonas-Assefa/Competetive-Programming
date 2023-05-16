class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def isSafe(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1
            for neighbor in graph[node]:
                if not isSafe(neighbor):
                    return False
            
            visited[node] = 2
            return True
        
        n = len(graph)
        visited = defaultdict(int)
        safe_states = []

        for node in range(n):
            if isSafe(node):
                safe_states.append(node)
        
        return safe_states