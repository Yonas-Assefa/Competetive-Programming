class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        row = len(grid)
        colm = len(grid[0])
        ans = [[0] * colm for i in range(row)]
 
        rowSum = [sum(i) for i in grid]
        colSum = [sum(i) for i in zip(*grid)]

        for i in range(row):
            onesRow = rowSum[i]
            zerosRow = row - onesRow
            for j in range(colm):
                onesCol = colSum[j]
                zerosCol = colm - onesCol
                diff = onesRow - zerosRow + onesCol - zerosCol
                ans[i][j] = diff
        return ans
                
                
                