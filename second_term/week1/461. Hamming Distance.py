class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y
        ansCount = 0
        
        while ans:
            if ans % 2 != 0:
                ansCount += 1
            ans = ans >> 1
        
        # while x or y:
        #     temp1 = x & 1
        #     temp2 = y & 1
        #     if temp1 != temp2:
        #         ansCount += 1
            
        #     x = x >> 1
        #     y = y >> 1

        
        return ansCount