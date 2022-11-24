class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        presum=[0]*len(nums)
        presum[0]=nums[0]
        for i in range(1,len(nums)):
            presum[i]=presum[i-1] + nums[i]
        maxL=presum[firstLen-1]
        maxM=presum[secondLen-1]
        ans=presum[firstLen+secondLen-1]
        for i in range(firstLen + secondLen,len(presum)):
            maxL=max(maxL,presum[i-secondLen]-presum[i-secondLen-firstLen])
            maxM=max(maxM,presum[i-firstLen]-presum[i-secondLen-firstLen])
            ans=max(ans,maxL + presum[i]-presum[i-secondLen],maxM+presum[i]-presum[i-firstLen])
        return ans
