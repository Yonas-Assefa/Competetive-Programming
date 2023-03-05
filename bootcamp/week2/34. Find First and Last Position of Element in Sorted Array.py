class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(leftMost: bool) -> int:
            low, high, result = 0, len(nums) - 1, -1
            
            # Repeat until the pointers low and high meet each other
            while low <= high:
                mid = (low + high) // 2                     # middle index - divide & conquer
                if target == nums[mid]:                     # target found
                    result = mid
                    if leftMost: high = mid - 1             # continue search for leftMost
                    else: low = mid +  1                    # continue search for rightMost
                elif target > nums[mid]: low = mid + 1      # target is on the right side
                else: high = mid - 1                        # target is on the left side
            
            return result
        return (binSearch(True), binSearch(False))   