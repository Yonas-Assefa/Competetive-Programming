class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        sumDict={0:1}
        s=0
        for i in nums:
            s+=i
            if s-k in sumDict:
                count+=sumDict[s-k]
            if s in sumDict:
                sumDict[s]+=1
            else:
                sumDict[s]=1
        return count
