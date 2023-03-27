class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        for i in range(3):
            lead = s[: i + 1]
            if self.isValid(lead, 0, i, s):
                self.ip([s[:i + 1]], self.ans, i + 1, s)

        return self.ans

    def ip(self, temp, ans, ind, s):

        if len(temp) == 4:
            val = ".".join(temp)
            
            if len(val) == len(s) + 3:
                # print(val, "val", ind)
                ans.append(val)
                return
            else:
                return

        for i in range(3):
            sec = s[ind : ind + i + 1]
            # print(sec, ind)
            if self.isValid(sec, ind, i, s):
                self.ip(temp + [s[ind : ind + i + 1]], ans, ind + i + 1, s)


    def isValid(self, ipStr, ind, i, s):
        print(ipStr, ind)
        if ipStr and (len(ipStr) == len(str(int(ipStr)))) and (int(ipStr) <= 255 )and (int(ipStr) >= 0) and (i + ind < len(s)):
            return True
        return False
        


