class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #DFS
        row = len(grid)
        col = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        res = 0

        def dfs(i, j):
            visited.add((i, j))
            for idx in range(4):
                newRow = i + directions[idx][0]
                newCol = j + directions[idx][1]
                # print("hre", newRow, newCol)
                if newRow in range(row) and newCol in range(col):
                    if grid[newRow][newCol] == "1" and (newRow, newCol) not in visited:
                        # print("kslkjslsjfk")
                        dfs(newRow, newCol)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    if (i, j) not in visited:
                        # print(visited)
                        # print(i, j)
                        res += 1
                        dfs(i, j)

        return res







#BFS
        row = len(grid)
        col = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        
        res = 0

        def bfs(i, j):
            islands = deque()
            islands.append((i, j))
            visited.add((i, j))
            while islands:
                cur = islands.popleft()
                for idx in range(4):
                    newRow = cur[0] + directions[idx][0]
                    newCol = cur[1] + directions[idx][1]
                    # print("hre", newRow, newCol)
                    if newRow in range(row) and newCol in range(col):
                        if grid[newRow][newCol] == "1" and (newRow, newCol) not in visited:
                            visited.add((newRow, newCol))
                            islands.append((newRow, newCol))
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    if (i, j) not in visited:
                        
                        # print(visited)
                        # print(i, j)
                        res += 1
                        bfs(i, j)

        return res