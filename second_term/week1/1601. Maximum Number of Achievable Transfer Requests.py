class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        building = [0 for _ in range(n)]
        self.n = len(requests)
        self.requests = requests
        self.ans = 0
        self.transfer(0, 0, building)
        return self.ans
    
    def transfer(self, ind, temp, building):
        if ind == self.n:
            if building.count(0) == len(building):
                self.ans = max(self.ans, temp)
            return
        out = self.requests[ind][0]
        enter = self.requests[ind][1]

        building[out] -= 1
        building[enter] += 1
        self.transfer(ind + 1, temp + 1, building)

        building[out] += 1
        building[enter] -= 1
        self.transfer(ind + 1, temp, building)


            
        

