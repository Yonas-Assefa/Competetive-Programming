class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(ind, prev):
            if ind == len(s):
                return True
            
            for j in range(ind, len(s)):
                val = int(s[ind: j + 1])
                if val + 1 == prev and dfs(j + 1, val):
                    return True
            return False
        for i in range(len(s) - 1):
            val = int(s[: i + 1])
            if dfs(i + 1, val):
                return True
        return False
