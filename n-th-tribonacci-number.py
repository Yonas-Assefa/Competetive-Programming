class Solution:
    def __init__(self):
        self.memo = {0:0,
                    1:1,
                    2:1}
    def tribonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        val = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        self.memo[n] = val
        return self.memo[n]