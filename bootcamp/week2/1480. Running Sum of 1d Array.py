class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        prev = 0
        for i in nums:
            prev += i
            ans.append(prev)
        return ans