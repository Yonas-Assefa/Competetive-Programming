class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums_len = len(nums)
        items_sum = (nums_len) * (nums_len + 1) // 2
        for i in nums:
            items_sum -= i
        return items_sum
        
        