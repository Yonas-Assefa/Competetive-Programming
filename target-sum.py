class Solution:
    def __init__(self):
        self.memo = {}
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def targetSum(curSum, ind):
            if (ind, curSum) in self.memo:
                return self.memo[(ind, curSum)]
            if ind == n:
                if curSum == target:
                    return 1
                return 0
            
            val = targetSum(curSum + nums[ind], ind + 1) + targetSum(curSum - nums[ind], ind + 1)
            self.memo[(ind, curSum)] = val
            return val
        
        return targetSum(0, 0)