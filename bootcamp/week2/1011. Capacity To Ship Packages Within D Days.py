class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        item = len(weights)
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            shiping_weights = left + (right - left) // 2
            sums = 0
            days_needed = 0
            for i in range(item):
                if (sums + weights[i]) <= shiping_weights:
                    sums += weights[i]
                else:
                    sums = weights[i]
                    days_needed += 1
            
            days_needed += 1
            
            if days_needed <= days:
                right = shiping_weights
            else:
                left = shiping_weights + 1
        
        return left
                
        