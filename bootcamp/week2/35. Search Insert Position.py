class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            ind = left + (right - left) //2
            if nums[ind] == target:
                return ind
            elif nums[ind] > target:
                right = ind - 1
            else:
                left = ind + 1
        
        return left
        