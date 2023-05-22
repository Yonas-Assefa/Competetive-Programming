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
            return True

        return False


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        self.points = points
        graph = self.buildGraph(n)
        pointDist = len(graph)
    
        uf = UnionFind(n)
        cost = 0
        # print(graph)
        for i in range(pointDist):
            dist, src, dest = graph[i]
            if uf.union(src, dest):
                # print(src, dest, dist)
                cost += dist

        return cost

    def buildGraph(self, n):
        graph = []
        for i in range(n):
            for j in range(i + 1, n):
                point1 = self.points[i]
                point2 = self.points[j]
                dist = self.calculateDistance(point1, point2)
                graph.append((dist, i, j))

        graph.sort(key = lambda x: x[0])
        return graph



    def calculateDistance(self, point1, point2):
        x1, x2 = point1[0], point2[0]
        y1, y2 = point1[1], point2[1]
        
        dist = abs(x2 - x1) + abs(y2 - y1)
        # print(point1, point2, dist)
        return dist