class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        if len(nums) ==2:return True
        difflect = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i - 1]:
                if difflect == 1:
                    return False
                difflect += 1
                '''
                the code below checks if the current element is less than or equal to thr previous two(i-1)
                element. if so,we can be sure that the deflected element is the current element and we will
                remove it by equalizing it the previous element. 6,7,2,8,9--6,7,7,8,9(we made it as if 2 has never even exist)
                But if it is not, we can be sure that it is the previous element difflected. since it is already become previous
                we ignore it once.1,2,6,3,4---just jump 6 
                '''
                if i > 1 and nums[i] <= nums[i-2]:
                    nums[i] = nums[i-1]
        return True
#