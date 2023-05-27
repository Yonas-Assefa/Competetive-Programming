class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.n = len(arr)
        self.maxSubstr = 0
        self.arr = arr

        for i in self.arr:
            if self.isUnique(i):
                self.maxConcat(1, i)

        return self.maxSubstr

    def maxConcat(self, ind, temp ):
        if ind < self.n:
            subStr = self.arr[ind]
            contains = False
            print(temp, subStr)
            for i in subStr:
                if i in temp:
                    contains = True
                    break
            
            if not contains and self.isUnique(subStr):
                self.maxConcat(ind + 1, temp + subStr)

            self.maxConcat(ind + 1, temp)
        print(self.maxSubstr, temp)
        self.maxSubstr = max(self.maxSubstr, len(temp))      
    
    def isUnique(self, subSeq):
        if len(set(subSeq)) == len(subSeq):
            return True
        return False