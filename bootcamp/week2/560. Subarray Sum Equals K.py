class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        sumDict={0:1}
        s=0
        for i in nums:
            s+=i
            diff=s-k
            count+=sumDict.get(diff,0)
            sumDict[s]=sumDict.get(s,0)+1
        return count