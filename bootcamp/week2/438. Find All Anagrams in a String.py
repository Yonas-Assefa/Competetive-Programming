class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pDict = Counter(p)
        p_len = len(p)
        s_len = len(s)
        sDict = Counter(s[0:p_len])
        res = []
        if pDict == sDict:
            res.append(0)
        
        for i in range(s_len - p_len):
            sDict[s[i]] -= 1
            if sDict[s[i]] == 0:
                del sDict[s[i]]
            sDict[s[i + p_len]] = sDict.get(s[i + p_len], 0) + 1
            
            if sDict == pDict:
                res.append(i + 1)
        return res
