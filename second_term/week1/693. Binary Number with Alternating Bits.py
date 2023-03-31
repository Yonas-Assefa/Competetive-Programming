class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None
        while n > 0:
            cur = n & 1
            if cur == prev:
                return False
            
            #update
            prev = cur
            n = n >> 1
        return True
