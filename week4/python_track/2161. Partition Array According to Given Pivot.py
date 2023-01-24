class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [pivot]
        num_len = len(nums)
        indx = 0

        for i in range(num_len):

            if nums[i] < pivot:
                ans.insert(indx, nums[i])
                indx += 1

            elif nums[i] > pivot:
                ans.append(nums[i])
            else:
                ans.insert(indx, nums[i])

        ans.pop(indx + 1)
        return ans

