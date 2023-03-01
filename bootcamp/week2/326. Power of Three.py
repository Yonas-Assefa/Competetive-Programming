class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True

        elif n < 1 or n % 3:
            return False

        return self.isPowerOfThree(n / 3)
        
        # if n == 1 or n == 3:
        #     return True
        # elif n < 1:
        #     return False
        # while not n % 3 and n != 3:
        #     n /= 3
        # return n % 3 == 0
