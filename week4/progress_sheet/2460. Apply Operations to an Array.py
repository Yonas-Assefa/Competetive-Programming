class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)

        for i in range(nums_len - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        seeker = 0
        placeholder = 0

        while seeker < nums_len:
            if nums[placeholder] != 0:
                placeholder += 1
                seeker += 1
            
            if nums[seeker] == 0:
                seeker += 1
            else:
                nums[seeker], nums[placeholder] = nums[placeholder], nums[seeker]
                seeker += 1
                placeholder += 1

        return nums
            
