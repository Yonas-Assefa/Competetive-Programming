class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        def returnMax(row, col):
            curMax = grid[row][col]
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    curMax = max(curMax, grid[i][j])
            return curMax

        
        ans = [[0 for _ in range(n - 2)] for _ in range(n - 2)]
        
        for i in range(n - 2):
            for j in range(n - 2):
                curMax = returnMax(i, j)
                ans[i][j] = curMax
        return ans