class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        jump = []
        
        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heappush(jump, diff)
            
            if len(jump) > ladders:
                bricks = bricks - heappop(jump)
            
            if bricks < 0:
                return i
        
        return (n - 1)