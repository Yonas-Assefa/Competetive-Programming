class Solution:    
    # def binary_search(self,low, high, b):
    #     if low > high:
    #         return False
    #     mid = low + ((high - low) // 2)
    #     if int((mid ** 2)) == b:
    #         return True
    #     elif int((mid ** 2)) > b:
    #         self.binary_search(low, mid - 1, b)
    #     else:
    #         self.binary_search(mid + 1, high, b)
    
    def judgeSquareSum(self, c: int) -> bool:
        # i = 0
        # while (i ** 2 ) <= c:
        #     b = c - (i ** 2) 
        #     if self.binary_search(0, b, b):
        #         return True
        #     i += 1
        # return False
        left = 0
        right = int(sqrt(c))

        while left <= right:
            tempSum = (left ** 2) + (right ** 2)
            if tempSum == c:
                return True
            elif tempSum > c: 
                right -= 1
            else: 
                left += 1
        
        return False





    #     rootC = int(c ** 0.5)
    #     low, high = 0, rootC
        
    #     while low <= high:
    #         result = low ** 2 + high ** 2
            
    #         if result == c:
    #             return True
    #         elif result > c:
    #             high -= 1
    #         else:
    #             low += 1
                
    #     return False

    