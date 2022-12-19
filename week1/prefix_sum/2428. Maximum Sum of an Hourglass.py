class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        if (row <3 or column < 3):
            return 0
        maxSum = 0
        for i in range(row-2):
            for j in range(column-2):
                tempSum = sum(grid[i][j:j+3]) + sum(grid[i+2][j:j+3]) + grid[i+1][j+1]
                print(tempSum)
                maxSum = max(tempSum,maxSum) 
        return maxSum
        