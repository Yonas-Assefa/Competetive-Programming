class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)  < len(t): return ""
        dict1, dict2, left, right, = {}, {}, 0, 0
        minLen, matchCount = len(s) + 1, 0
        leftP = 0
        rightP = 0
        for i in t:
            dict1[i] = dict1.get(i,0) + 1
            
        while right < len(s):
            if s[right] in dict1:
                dict2[s[right]] = dict2.get(s[right], 0) + 1
                if dict2[s[right]] == dict1[s[right]]:
                    matchCount += 1
            while matchCount == len(dict1):
                if minLen > (right - left + 1):
                    minLen = right - left + 1
                    leftP = left
                    rightP = right + 1
                if s[left] in dict2:
                    dict2[s[left]] -= 1
                    if dict2[s[left]] < dict1[s[left]]:
                        matchCount -= 1
                    if dict2[s[left]] == 0:
                        del dict2[s[left]]
                left += 1
            right += 1
        return (s[leftP:rightP])