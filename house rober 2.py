class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]    
        def rob(cur, num, memo):
            if cur in memo:
                return memo[cur]

            if cur == n - 2:
                return num[n - 2]
            if cur == n - 3:
                return max(num[n - 2], num[n - 3])
            
            res =  max(rob(cur + 1, num, memo), num[cur] + rob(cur + 2, num, memo))
            memo[cur] = res 
            return memo[cur]
         
        ans = rob(0, nums[ : n - 1], {})
        ans2 = rob(0, nums[1: n], {})
        return max(ans, ans2)

        # 1000140041126