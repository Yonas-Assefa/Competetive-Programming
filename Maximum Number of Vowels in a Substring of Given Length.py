class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vwl=['a','e','i','o','u']
        count=0
        maxCount=0
        for i in range(k):
            if s[i] in vwl:count+=1
        l=0
        r=k
        while r<len(s):
            maxCount=max(maxCount,count)
            if s[l] in vwl:count-=1
            if s[r] in vwl:count+=1
            
            l+=1
            r+=1
        maxCount=max(maxCount,count)
        return maxCount
        
        
