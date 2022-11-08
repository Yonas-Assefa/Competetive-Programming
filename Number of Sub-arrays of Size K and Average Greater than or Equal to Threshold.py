class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        preSum=sum(arr[:k])
        if preSum/k >=threshold:
            ans=1
        else:
            ans=0
        L=0
        R=k
        while R<len(arr):
            preSum=preSum-arr[L]+arr[R]
            if preSum/k >=threshold:
                ans+=1
            L+=1
            R+=1
        return ans
