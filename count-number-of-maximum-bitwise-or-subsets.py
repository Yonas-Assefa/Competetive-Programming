class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.orEd = nums[0]
        self.n = len(nums)
        self.count = 0
        self.nums = nums
        for i in range(1, self.n):
            self.orEd = self.orEd | nums[i]
        

        self.subSet([], 0, 0)
     
        return self.count

    
    def subSet(self, temp, curOr, ind):
        if ind == self.n:
            if curOr == self.orEd:
                self.count += 1
            return
        
        self.subSet(temp + [self.nums[ind]], curOr | self.nums[ind], ind + 1)
        self.subSet(temp, curOr, ind + 1)

        # if curOr == self.orEd:
        #     print(temp, curOr)
        #     self.count += 1
            










        # print(temp, curOr,"above")
        # if curOr == self.orEd:
        #     self.count += 1
        # if ind == self.n:
        #     return
        
        # temp.append(self.nums[ind])
        # curOr = curOr | self.nums[ind]
        # self.subSet(temp, curOr, ind + 1)

        # curOr = curOr ^ self.nums[ind]
        # temp.pop()
        # print(temp, curOr, 'below')