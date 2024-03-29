class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price, max_price = prices[0], prices[0]
        
        for i in range(1, len(prices)):
            
            if prices[i] < min_price:
                min_price, max_price = prices[i], prices[i]
                
            elif prices[i] > max_price:
                max_price = prices[i]
                profit = max(profit, max_price - min_price)

        return profit