class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m-2,-1,-1):
            curr=matrix[i][0]
            row=i
            col=0
            while row<m and col<n:
                if curr!=matrix[row][col]:
                    return False
                row+=1
                col+=1
        for i in range(1,n):
            curr=matrix[0][i]
            row=0
            col=i
            while row<m and col<n:
                if curr!=matrix[row][col]:
                    return False
                row+=1
                col+=1
        return True