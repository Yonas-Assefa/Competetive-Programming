class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for src, dest, distance in roads:
            adjList[src].append((dest, distance))
            adjList[dest].append((src, distance))


        def dfs(cur):
            if cur in visited:
                return
            visited.add(cur)
            nonlocal res
            for dest, dist in adjList[cur]:
                res = min(dist, res)
                dfs(dest)
        
        visited = set()
        res = float("inf")
        dfs(1)
        return res