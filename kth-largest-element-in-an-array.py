class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a = []
        heapify(a)
        for i in range(k):
            heappush(a, nums[i])
        print(a)
        for i in range(k, len(nums)):
            if a[0] <= nums[i]:
                heappop(a)
                heappush(a, nums[i])
        print(a)
        return min(a)