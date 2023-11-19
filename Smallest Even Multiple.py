class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        while n % 2 == 0:
            return n
        
        return (n * 2)
        
