class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        d = {(1,0):1,(1,1):1}

        def helper(i, j):
            if (i,j) in d:
                return d[(i,j)]
            if j == 0 or j == i:
                return 1
            val = (helper(i - 1, j) + helper(i - 1, j - 1))
            d[(i,j)] = val
            return d[(i,j)]
        ans = [0 for z in range((rowIndex + 1))]

        for p in range(rowIndex + 1):
            val = helper(rowIndex, p)
            ans[p] = val
        return ans
        
        