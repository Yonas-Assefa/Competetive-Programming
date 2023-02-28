class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        n = len(nums)
        total = sum(nums[left: right])
        max_sum = total
        while right < n:
            diff = nums[right] - nums[left]
            total += diff
            max_sum = max(max_sum, total)

            left += 1
            right += 1
        
        return (max_sum / k)
        


            
