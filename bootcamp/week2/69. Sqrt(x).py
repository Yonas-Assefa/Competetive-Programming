class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            if right - left <= 1:
                if right ** 2 == x:
                    return right
                return left
            mid = left + ((right - left) // 2)
            val = mid ** 2
            if val == x:
                return mid
        
            elif val > x:
                right = mid
            else:
                left = mid
            
                
