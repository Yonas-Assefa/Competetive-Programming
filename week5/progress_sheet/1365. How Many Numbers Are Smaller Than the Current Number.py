class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        left = 0
        right = 0
        ans = []
        count = 0
        while left < len(nums) and right < len(nums):
            
            if left != right:
    
                if nums[right] < nums[left]:
                    count += 1
                    right += 1
                else:
                    right += 1
            else:
                right += 1

            if right == len(nums):
                ans.append(count)
                count = 0
                right = 0
                left += 1
        return ans
