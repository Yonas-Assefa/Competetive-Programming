class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n == 4 or n == 1:
        #     return True
        # elif n % 4 or n <= 0:
        #     return False

        # return self.isPowerOfFour(n / 4)
        
        if n == 1 or n == 4:
            return True
        elif n <= 0:
            return False
        
        while not n % 4 and n != 4:
            n /= 4
        
        return n % 4 == 0