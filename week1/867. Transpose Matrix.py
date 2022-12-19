class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        rowT = col
        colT = row
        ans = [[0]*colT for i in range(rowT)]
        print(ans)
        for i in range(row):
            for j in range(col):
                ans[j][i]= matrix[i][j]
        return ans