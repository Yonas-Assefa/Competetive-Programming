class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLen = 0
        count = 0
        sumDict = {0:-1}
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1 
            else:
                count -=1

            if count in sumDict:
                maxLen = max(maxLen, i - sumDict[count])
            else:
                sumDict[count] = i
        return maxLen
        
                