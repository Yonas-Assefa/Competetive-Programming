class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        opr_num = len(operations)
        nums_len = len(nums)
        nums_dict = {}

        for i in range(nums_len):
            nums_dict[nums[i]] = i

        for i in range(opr_num):
            old_value = operations[i][0]
            new_value = operations[i][1]

            indx = nums_dict[old_value]
            nums[indx] = new_value
            del nums_dict[old_value]
            nums_dict[new_value] = indx

        return nums