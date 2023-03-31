class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.validSebseq = {}
        self.nums = nums
        self.n = len(nums)

        for i in range(self.n):
            self.findSubseq(i + 1, [self.nums[i]])
        print(self.validSebseq)
        return self.validSebseq
    

    def findSubseq(self, ind, temp):
        if ind < self.n:
            if temp[-1] <= self.nums[ind]:
                self.findSubseq(ind + 1, temp + [self.nums[ind]])
            self.findSubseq(ind + 1, temp)
        
        if len(temp) >= 2:
            tup = tuple(temp)
            self.validSebseq[tup] = self.validSebseq.get(tup, 0) + 1
