class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        heapify(heap)
        for i in piles:
            heappush(heap, -1 * i)
        
        for i in range(k):
            maxPile = heappop(heap)
            # print(maxPile)
            oper = floor(maxPile / 2)
            heappush(heap, oper)
        
        return (-1 * sum(heap))