class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        diffDict = {}
        for num in arr:
            if num - difference in diffDict:
                diffDict[num] = diffDict[num - difference] + 1
            else:
                diffDict[num] = 1
        
        return max(diffDict.values())