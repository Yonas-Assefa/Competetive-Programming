class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        if n <= 4:
            return 0
        minDiff = float("inf")
        right = -4
        left = 0

        for i in range(4):
            minDiff = min(minDiff, nums[right] - nums[left])
            left += 1
            right += 1

            # changeFirst3 = nums[-1] - nums[3]
            # changeLast3 = num[-4] - nums[0]
            # changeFirst2 = nums[-2] - nums[2]
            # changeLast2 = nums[-3] - nums[1]
        return minDiff