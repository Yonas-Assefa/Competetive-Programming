class Solution:
    def sortSentence(self, s: str) -> str:
        sentArray=s.split()
        sentArrayNumber=[]
        for i in sentArray:
            sentArrayNumber.append(eval(i[-1]))
        sentArrayNumber.sort()
        sortedSentArray=[]
        for i in sentArrayNumber:
            for j in sentArray:
                if eval(j[-1])==i:
                    j=j[:-1]
                    sortedSentArray.append(j)
        s=' '.join(sortedSentArray)
        return s
