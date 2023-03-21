class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        self.ans = float("inf")
        tempDistribution = [0] * k

        self.distributer(0, cookies, tempDistribution, n, k, self.ans)
        return self.ans

    
    def distributer(self, ind, cookies, tempDistribution, n, k, ans):
        if ind == n:
            self.ans = min(ans, max(tempDistribution))
            return
        
        for i in range(k):
            if tempDistribution[i] + cookies[ind] < self.ans:
                tempDistribution[i] += cookies[ind]
                self.distributer(ind + 1, cookies, tempDistribution, n, k, ans)
                tempDistribution[i] -= cookies[ind]
        
        return

        
