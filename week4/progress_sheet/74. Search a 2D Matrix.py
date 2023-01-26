class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num = len(matrix)
        col_num = len(matrix[0])

        for i in range(row_num):
            if target <= matrix[i][col_num - 1]:
                for j in range(col_num):
                    if target == matrix[i][j]:
                        return True
                return False