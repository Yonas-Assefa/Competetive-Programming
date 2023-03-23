class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        return self.devide(left, right, nums)

    def devide(self, left, right, nums):
        if left == right:
            return [nums[left]]
        
        mid = left + (right - left) // 2
        left = self.devide(left, mid, nums)
        right = self.devide(mid + 1, right, nums)
        
        return self.merge(left, right)
    
    def merge(self, list1, list2):
        top = 0
        botm = 0
        res = []

        while top < len(list1) and botm < len(list2):
            if list1[top] <= list2[botm]:
                res.append(list1[top])
                top += 1
            else:
                res.append(list2[botm])
                botm += 1
        
        res += list1[top: ]
        res += list2[botm: ]
                
        return res
    
