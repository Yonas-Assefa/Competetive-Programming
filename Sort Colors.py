class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            l=0
            r=1
            while r<len(nums)-i:
                if nums[l]>nums[r]:
                    nums[l],nums[r]=nums[r],nums[l]
                r+=1
                l+=1
            
            
        
