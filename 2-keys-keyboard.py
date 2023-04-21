class Solution:
    def minSteps(self, n: int) -> int:
        count = 0
        prime = 2
        while prime * prime <= n:

            while n % prime == 0:
                count += prime
                n //= prime
            
            prime += 1
        
        if n > 1:
            count += n
        return count