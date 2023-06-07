class Solution:
    def numDecodings(self, s: str) -> int:
        # dp = {}
        # def findWay(ind):
        #     if ind < n and s[ind] == "0":
        #         return 0
            
        #     if ind >= (n - 1):
        #         return 1
            
        #     if ind in dp:
        #         return dp[ind]
            
        #     if (ind + 1) in range(n) and int(s[ind] + s[ind + 1]) in range(27):
        #         dp[ind] = findWay(ind + 1) + findWay(ind + 2)
        #     else:
        #         dp[ind] = findWay(ind + 1)

        #     return dp[ind]
        
        # n = len(s)
        # return findWay(0)


        n = len(s)
        dp = {n : 1}

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            
            elif (i + 1) in range(n) and int(s[i] + s[i + 1]) in range(27):
                dp[i] = dp[i + 1] + dp[i + 2]

            else:
                dp[i] = dp[i + 1]    
        return dp[0]