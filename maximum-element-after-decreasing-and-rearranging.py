class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        count = 0
        if arr[0] != 1:
            arr[0] = 1

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < 0:
                diff *= -1
            if diff > 1:
                arr[i] = arr[i - 1] + 1
        
        return max(arr)