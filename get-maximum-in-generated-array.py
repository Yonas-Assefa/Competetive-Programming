class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # nums = [0 for i in range(n + 1)]
        # nums[0] = 0
        # nums[1] = 1
        memo = {0:0, 1:1}
        def elem(cur):
            if cur in memo:
                return memo[cur]
            if cur % 2 != 0:
                temp = cur // 2
                val = elem(temp) + elem(cur - temp)
                memo[cur] = val
                return memo[cur]
            else:
                val = elem(cur // 2)
                memo[cur] = val
                return memo[val]

        maxNum = -float("inf")
        for i in range(n + 1):
            val = elem(i)
            print(val)
            maxNum = max(maxNum, val)
        return maxNum