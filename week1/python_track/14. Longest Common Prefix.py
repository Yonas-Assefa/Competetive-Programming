class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minStr = float("inf")
        for i in strs:
            minStr = min(minStr, len(i))
        longPrefix = ""
        for i in range(minStr):
            char = strs[0][i]
            for j in range(len(strs)):
                if char != strs[j][i]:
                    return longPrefix
            longPrefix += char
        return longPrefix
        """
        -time complexity == O(n * m)
            where n = len of  the shortest string 
                  m = len of the given array
        -space complexity == O(1):
            since we haven't used any extra space
        """