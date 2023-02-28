class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = 0
        mx_len = 0
        
        while right < len(s):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            mx_len = max(mx_len, right - left + 1)
            seen.add(s[right])
            right += 1

        return mx_len