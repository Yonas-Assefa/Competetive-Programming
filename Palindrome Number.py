class Solution:
    def isPalindrome(self, x: int) -> bool:
        posNum = x
        if x < 0:
            posNum = x * -1

        reverse = 0

        while posNum > 0:
            rem = posNum % 10
            reverse = (reverse * 10) + rem
            posNum //= 10
      
        return (reverse == x)
        
        
