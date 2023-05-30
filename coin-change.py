class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # n = len(coins)
        # minChanges = [(amount + 1) for _ in range(amount + 1)]
        # minChanges[0] = 0

        # for i in range(1, amount + 1):
        #     for coin in coins:
        #         diff = i - coin
        #         if diff >= 0:
        #             minChanges[i] = min(minChanges[i], minChanges[diff] + 1) 
        
        # return -1 if minChanges[-1] > amount else minChanges
        
        memo = {}
        def coinChange(curVal):
            
            if curVal == 0:
                return 0

            if curVal in memo:
                return memo[curVal]

            minVal = amount + 1

            for i in coins:
                diff = curVal - i
                if diff >= 0:
                    minVal = min(minVal, coinChange(diff) + 1)
                
            memo[curVal] = minVal     
            return memo[curVal]
        
        minChange = coinChange(amount)
        return minChange if minChange <= amount else -1