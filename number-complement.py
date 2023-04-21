class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        count = 0
        while num:
            temp = num & 1
            if not temp:
                added = 2 ** count
                ans += added
            # else:
            #     added = 2 ** count
            #     ans += added
            num =  num >> 1
            count += 1

        return ans