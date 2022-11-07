class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=len(nums)+1
        tempSum,l,r,=0,0,0
        for r in range(len(nums)):
            tempSum=tempSum+nums[r]
            while tempSum>=target:
                res=min(r-l+1,res)
                tempSum-=nums[l]
                l+=1
        return res if res<=len(nums) else 0
            
