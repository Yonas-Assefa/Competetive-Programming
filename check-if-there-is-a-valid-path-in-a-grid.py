class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.streets = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)],
        }
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.target = (self.m - 1, self.n - 1)
        self.visited = set()

        return self.dfs(0, 0)


    def dfs(self, row, col):
        if (row, col) == self.target:
            return True

        self.visited.add((row, col))
        pathVal = self.grid[row][col]
        # print(self.visited)

        for i in range(2):
            path = self.streets[pathVal][i]
            nextPath = (row + path[0], col + path[1])
        
            if self.validGrid(nextPath[0], nextPath[1]):
                if nextPath not in self.visited:
                    # print(nextPath[0], nextPath[1])
                    nextPathValue = self.grid[nextPath[0]][nextPath[1]]
                    reversePath = (path[0] * -1, path[1] * -1)
                    if reversePath in self.streets[nextPathValue]:
                        if self.dfs(nextPath[0], nextPath[1]):
                            return True
        return False
    
    def validGrid(self, row, col):
        
        if row < self.m and row >= 0 and col < self.n and col >= 0:
            # print(row, col)
            return True
        return False