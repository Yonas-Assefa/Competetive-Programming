class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        n = len(nums1)
        m = len(nums2)
        
        for i in range(min(k, n)):
            for j in range(min(k, m)):
                curSum = -1 * (nums1[i] + nums2[j])
                if len(heap) < k:
                    heappush(heap, (curSum, nums1[i], nums2[j]))
                else:
                    if -1 * curSum > -1 * heap[0][0]:
                        break
                    else:
                        heappushpop(heap, (curSum, nums1[i], nums2[j]))
                        
        return [[first, second] for (_, first, second) in heap]