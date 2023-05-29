class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {n - 2 : 0, n - 1: 0}

        def stairCost(i, n, cost):
            # if (i + 2) >= n:
            #     return 0
            if i in cache:
                return cache[i]
            val = min(cost[i + 1] + stairCost(i + 1, n, cost), cost[i + 2] + stairCost(i + 2, n, cost))
            cache[i] = val
            return cache[i]
        
        minCost = stairCost(-1, n, cost)

        return minCost