class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,1
        if s:
            temp=s[i]
            maxC=0
            while j<len(s):
                if s[j] not in temp:
                    temp+=s[j]
                    j+=1
                    maxC=max(maxC,len(temp))
                else:
                    tempS=s[:j]
                    tempIndex=tempS.rfind(s[j])+1
                    temp=s[tempIndex:j+1]
                    j+=1

            if maxC==0:
                return 1
            else:
                return maxC
        else:
            return 0
                
