class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if (k * 2) + 1 > len(nums):
            return [-1] * (len(nums))
        
        ans = [-1] * k
        diameter = (k * 2) + 1
        left = 0
        right = diameter
        
        radSum = sum(nums[left:right])
        ans.append( radSum // diameter )
        
        
        while right < len(nums):
            radSum = radSum - nums[left] + nums[right]
            ans.append(radSum // diameter)
            left += 1
            right += 1
        for i in range(k):
            ans.append(-1)
        return ans
                