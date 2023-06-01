class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                diff =  i - num
                if diff >= 0:
                    dp[i] += dp[diff]
        
        return dp[-1]

        # def comb(curSum):
        #     if curSum in memo:
        #         return memo[curSum]
        #     if curSum == 0:
        #         return 1

        #     if curSum < 0:
        #         return 0

        #     # if ind >= n:
        #     #     return 0
        #     total = 0
        #     for num in nums: 
        #         diff = curSum - num
        #         ways = comb(diff)
        #         total += ways
        #         memo[diff] = ways
            
        #     memo[curSum] = total
        #     return memo[curSum]
        
        # memo = {}
        # return comb(target)