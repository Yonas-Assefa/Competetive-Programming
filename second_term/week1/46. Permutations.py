class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.ans = []

        for i in range(self.n):
            self.permutuation([nums[i]], nums[ : i] + nums[i + 1 :])
            
        return self.ans
    
    def permutuation(self, temp, num):
        if not num:
            self.ans.append(temp)
            return

        for i in range(len(num)):

            self.permutuation(temp + [num[i]], num[ : i] + num[i + 1 :] )
        
        

