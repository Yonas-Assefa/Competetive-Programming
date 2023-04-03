class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxNum = max(nums)
        minNum = min(nums)
        ans = self.GCD(minNum, maxNum)
        return ans
    
    def GCD(self, num1, num2):
        if num2 == 0:
            return num1
        return self.GCD(num2, num1 % num2)
