class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        len1 = len(word1)
        len2 = len(word2)

        for i in range(min(len1, len2)):
            ans += word1[i]
            ans += word2[i]
        
        if len1 < len2:
            ans += word2[len1 : len2]
        elif len2 < len1:
            ans += word1[len2 : len1]
        
        return ans
        
