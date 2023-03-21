class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        res = [["."] * n for _ in range(n)]

        def isValidGrid(n, row, col, res):
            left = col
            right = col

            while row >= 0:
                
                if (res[row][col] == "Q") or ((left >= 0) and res[row][left] == "Q"):
                    return False
                elif ((right < n) and res[row][right] == "Q"):
                    return False

                row -= 1
                left -= 1
                right += 1

            return True

        def placement(n, row, res,ans):
            if row == n:
                return 1

            for col in range(n):
                if isValidGrid(n, row, col, res):
                    res[row][col] = "Q"
                    ans += placement(n, row + 1, res,0)
                    res[row][col] = "." 
            return ans
        
        return placement(n, 0, res,ans)
        