class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i=0
        j=1
        count=0
        while i<len(nums)-1:
            if nums[i]==nums[j]:
                count+=1
            if j==len(nums)-1:
                i+=1
                j=i+1
                continue
            j+=1
        return count
        
