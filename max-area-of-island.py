class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        self.n = len(grid)
        self.m = len(grid[0])
        self.grid = grid
        self.visited = set()

        for i in range(self.n):
            for j in range(self.m):
                self.count = 0
                self.dfs((i, j))
                maxArea = max(maxArea, self.count)

        return maxArea
    
    def dfs(self, curCell):
        if curCell not in self.visited:
            self.visited.add(curCell)
            curRow = curCell[0]
            curCol = curCell[1]
        
            if self.isValidCell(curCell) and self.grid[curRow][curCol] == 1:
                self.count += 1

                self.dfs((curRow - 1, curCol))
                self.dfs((curRow, curCol - 1))
                self.dfs((curRow + 1, curCol))
                self.dfs((curRow, curCol + 1))

    


    def isValidCell(self, cell):
        row = cell[0]
        col = cell[1]
        if row < self.n and row >= 0 and col < self.m and col >= 0:
            return True
        else:
            return False