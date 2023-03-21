class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        print(nums)
        self.ans = []
        res = []
        self.combinator(self.ans, res, 0, nums, k)
        return self.ans

    def combinator(self, ans, res, ind, nums, k):
        #base cases
        if len(res) == k:

            self.ans.append(res.copy())
            return
            # res.pop()
            # self.combinator(self.ans, res, ind, nums, k)
       
        if ind == len(nums):
            return
       
        res.append(nums[ind])
        self.combinator(self.ans, res, ind + 1, nums, k)
        res.pop()
        self.combinator(self.ans, res, ind + 1, nums, k)

    


        

            



        