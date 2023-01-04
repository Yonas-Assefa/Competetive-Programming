class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) < (len(words)*len(words[0])):return []
        
        wordLen = len(words[0])
        noWords = len(words)
        left, right, ans = 0, wordLen * noWords, []
        dict1 = {}
        for i in words:
            dict1[i] = dict1.get(i, 0) + 1
        
        while right <= (len(s)):
            dict2 = {}
            subStr= s[left:right]
            for i in range(noWords):
                temp = subStr[(i * wordLen): (i * wordLen)+wordLen]
                if temp in dict1:
                    dict2[temp] = dict2.get(temp, 0) + 1
            if dict1 == dict2:
                ans.append(left)
            right += 1
            left += 1
            
        return ans
        