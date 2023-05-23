class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row = len(grid1)
        col =  len(grid1[0])
        visit = set()
        res = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def colorize(i, j):
            if grid2[i][j] == 0:
                return
            visit.add((i, j))
            grid2[i][j] = 0
            for rw, cl in directions:
                newRow = i + rw
                newCol = j + cl
                if newRow in range(row) and newCol in range(col):
                    if grid2[newRow][newCol] == 1 and (newRow, newCol) not in visit:
                        colorize(newRow, newCol)

       
        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    colorize(i, j)
    
        
        visited = set()
        

        def dfs(i, j):
            visited.add((i, j))
            for rw, cl in directions:
                newRow = i + rw
                newCol = j + cl
                
                if newRow in range(row) and newCol in range(col):
                    if grid2[newRow][newCol] == 1 and (newRow, newCol) not in visited:
                        dfs(newRow, newCol)

        

        # print(type(grid1[0][0]))
        # print(grid2)

        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1:

                    if (i, j) not in visited:
                        # print(i,j)
                        res += 1
                        dfs(i, j)
        
        return res