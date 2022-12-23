class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        letter_count = {}
        count = 0

        for i in nums:
            letter_count[i] = letter_count.get(i, 0) + 1
 
        for i in letter_count:
            no_of_combination = (letter_count[i] * (letter_count[i] - 1)) // 2
            count  += no_of_combination
            
        return count