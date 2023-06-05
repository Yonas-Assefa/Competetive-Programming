class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # dp = {}
        # n = len(questions)

        # def maxEarn(ind):
        #     if ind >= n:
        #         return 0
            
        #     if ind in dp:
        #         return dp[ind]
            
        #     way1 = maxEarn(ind + 1)
        #     way2 = questions[ind][0] + maxEarn(ind + questions[ind][1] + 1)
        #     dp[ind] = max(way1, way2)
            
        #     return dp[ind]
        
        # return maxEarn(0)

        #bottom-up dp
        dp = defaultdict(int)
        n = len(questions)
        for i in range(n - 1, -1, -1):
            path1 = questions[i][0] + dp[i + questions[i][1] + 1] 
            path2 = dp[i + 1]
            dp[i] = max(path1, path2)
        
        return dp[0]