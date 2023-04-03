# class Solution:
#     def subarrayGCD(self, nums: List[int], k: int) -> int:
#         left = 0
#         right = 1
#         last = 0
        
#         n = len(nums)

#         count = 0
#         while right < n:
#             if nums[left] == k:
#                 count += 1
#             gcd = None

#             if nums[left] == nums[right]:
#                 gcd = 1
#             else:
#                 gcd = self.GCD(nums[left], nums[right])
#             if gcd == k:
#                 count += (right - last)
#             else:
#                 last = right
#             print(count, left, right, last)
#             left += 1
#             right += 1
            

#         if nums[left] == k:
#             count += 1


            
        
#         return count
    
#     def GCD(self, num1, num2):
#         if num2 == 0:
#             return num1
        
#         return self.GCD(num2, num1 % num2)


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            temp = nums[i]
            for j in range(i, n):
                temp = math.gcd(temp, nums[j])
                if temp == k:
                    ans += 1
                elif temp < k:
                    break
        return ans
