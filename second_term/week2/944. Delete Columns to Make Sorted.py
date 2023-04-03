class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        self.strs = strs
        row = len(strs)
        col = len(strs[0])
        res = 0

        for i in range(col):
            if not self.isSorted(i, row):
                res += 1
        return res

    def isSorted(self, curCol, row):
        prev = 0
        for j in range(row):
           
            temp = ord(self.strs[j][curCol])
            if temp < prev:
                return False
            prev = temp
         
        return True

