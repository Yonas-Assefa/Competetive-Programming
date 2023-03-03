class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROW, COLUMN = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (COLUMN+1) for r in range(ROW+1)]
        
        for r in range(ROW):
            prefix = 0
            for c in range(COLUMN):
                prefix += matrix[r][c]
                above = self.sumMatrix[r][c+1]
                self.sumMatrix[r+1][c+1] += prefix + above
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        bottomSum = self.sumMatrix[row2][col2]
        aboveSum = self.sumMatrix[row1-1][col2]
        leftSum = self.sumMatrix[row2][col1-1]
        upperLeftSum = self.sumMatrix[row1-1][col1-1]
        return bottomSum - aboveSum - leftSum + upperLeftSum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
