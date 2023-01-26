class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # dup_count = 0
        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     if nums[left] == nums[left + 1]:
        #         value = nums.pop(left + 1)
        #         nums.append(value)
        #         dup_count += 1
        #         right -= 1
        #     else:
        #         left += 1
        # return (len(nums) - dup_count)

        left = 1
        
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1

        return left
