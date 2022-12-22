class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        rightP = len(s) - 1

        while rightP >= 0:
            if s[rightP] == "#":
                number = int(s[rightP - 2: rightP])
                char = chr(number + 96)
                ans = char + ans
                rightP -= 3
            else:
                number = int(s[rightP])
                char = chr(number + 96)
                ans = char + ans
                rightP -= 1
        return ans


