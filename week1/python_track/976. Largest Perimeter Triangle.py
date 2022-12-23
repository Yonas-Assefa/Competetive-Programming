class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        nums_len = len(nums)
        max_perimeter = 0
        for i in range(nums_len - 2):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                perimeter = nums[i] + nums[i + 1] + nums[i + 2]
                max_perimeter = max(max_perimeter, perimeter)
        return max_perimeter
        
