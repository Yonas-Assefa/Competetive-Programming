class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        leng = (2 ** n) - 1
        prev = (2 ** (n - 1)) - 1

        if k == (leng // 2) + 1:
            return "1"
        
        if k <= prev:
            return self.findKthBit(n - 1, k)
        else:
            return str(1 - int(self.findKthBit(n - 1, leng - k + 1)))


        