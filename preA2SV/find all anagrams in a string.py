class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):return []
        sCount,pCount,res={},{},[]
        for c,ltr in enumerate(p):
            pCount[ltr]=pCount.get(ltr,0)+1
            sCount[s[c]]=sCount.get(s[c],0)+1
        if pCount==sCount:res.append(0)
        l=0
        for r in range(len(p),len(s)):
            sCount[s[r]]=sCount.get(s[r],0)+1
            sCount[s[l]]-=1
            if sCount[s[l]]==0:
                del sCount[s[l]]
            l+=1
            if sCount==pCount:
                res.append(l)
        return res
            
