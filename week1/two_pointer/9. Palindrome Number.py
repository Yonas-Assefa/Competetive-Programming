class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        # ans = []
        # while x > 0:
        #     rem = x % 10
        #     ans.append(rem)
        #     x = x //10
        # left = 0
        # right = len(ans)-1

        # while left < right:
        #     if ans[left] == ans[right]:
        #         left += 1
        #         right -= 1
        #     else:
        #         return False
        # return True
        """
        -this solution has space complexity of O(n) since we used 
        an extra list to save the num digits
        """
        #another solution without using space
        if x < 0:
            return False
        num = x
        revNum = 0
        while x > 0:
            revNum = (revNum * 10) + (x % 10)
            x //= 10
        return num == revNum
        """
        -this solution has time complexity of O(log(10)n) because we iterate (number of digits of the given number)times
        -since we dont use any space we have O(1)
        """