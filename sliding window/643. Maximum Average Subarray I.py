class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right, windowSum = 0, k, sum(nums[:k])
        maxAverage = windowSum / k
        while right < len(nums):
            windowSum = windowSum + nums[right] - nums[left]
            maxAverage = max(maxAverage, windowSum/k)
            right += 1
            left += 1
        return maxAverage
            