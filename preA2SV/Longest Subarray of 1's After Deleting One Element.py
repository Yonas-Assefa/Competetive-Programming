class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        L=0
        R=0
        maxCount=0
        count=0
        zeroCount=0
        while R<len(nums):
            if nums[R]==0:
                zeroCount+=1
            if zeroCount==2:
                count=R-L-1
                maxCount=max(maxCount,count)
            while zeroCount==2:
                if nums[L]==0:
                    zeroCount-=1
                L+=1
            R+=1
        return max(maxCount,R-L-1)
