class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = { (m - 1, n - 2) : 1, (m - 2, n - 1) : 1}
        directions = [ (0, 1), (1, 0)]
        if n == 1 and m == 1:
            return 1
        def findPath(curLoc):
            if curLoc in memo:
                return memo[curLoc]
            uniqPath = 0
            for pos in directions:
                nxtRow = curLoc[0] + pos[0]
                nxtCol = curLoc[1] + pos[1]
                
                if nxtRow in range(m) and nxtCol in range(n):
                    uniqPath += findPath((nxtRow, nxtCol))
            
            memo[curLoc] = uniqPath
            return memo[curLoc]
        
        return findPath((0, 0))