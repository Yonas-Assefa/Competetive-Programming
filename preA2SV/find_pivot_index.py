class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        leftsum=0
        ans=-1
        for i in range(len(nums)):
            s=s-nums[i]
            if leftsum==s:
                ans=i
                break
            leftsum+=nums[i]
        return ans
        
