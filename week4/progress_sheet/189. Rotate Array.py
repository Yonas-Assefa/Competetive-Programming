class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     temp=nums.pop()
        #     nums.insert(0,temp)
        def reverse_array(array, left, right):
            while left < right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
                
            return array
        k =  k % len(nums)
        nums_reversed = reverse_array(nums, 0, len(nums) - 1)
        reverse_array(nums_reversed, 0, k - 1)
        reverse_array(nums_reversed, k, len(nums) - 1)

    
    


        