class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
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

        def placement(n, row, res):
            if row == n:
                temp = ["".join(resRow) for resRow in res]
                ans.append(temp)
                return

            for col in range(n):
                if isValidGrid(n, row, col, res):
                    res[row][col] = "Q"
                    placement(n, row + 1, res)
                    res[row][col] = "."           
        
        placement(n,0, res)
        return ans
