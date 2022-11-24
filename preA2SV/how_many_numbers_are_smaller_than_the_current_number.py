class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            output.append(0)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j] and i!=j:
                    output[i]+=1
        return output
