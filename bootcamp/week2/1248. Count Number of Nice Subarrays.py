class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        prefix={0:1}
        tempSum=0
        ans=0
        for i in nums:
            tempSum=tempSum+i
            prefix[tempSum]=prefix.get(tempSum,0)+1
            ans=ans+prefix.get(tempSum-k,0)
        return ans
        
        