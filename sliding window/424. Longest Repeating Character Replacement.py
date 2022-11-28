class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, strCount, maxLen, maxRepeated = 0, 0, {}, 0, 0
        while right < len(s):
            strCount[s[right]] = strCount.get(s[right], 0) + 1
            maxRepeated = max(maxRepeated, strCount[s[right]])
            if right - left + 1 - maxRepeated > k:
                strCount[s[left]] -= 1
                if strCount[s[left]] == 0:
                    del strCount[s[left]]
                left += 1
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen
    