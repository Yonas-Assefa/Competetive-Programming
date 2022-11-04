class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k>len(cardPoints):return 0
        l=0
        r=len(cardPoints)-k
        total=sum(cardPoints[r:])
        maxSum=total
        while r<len(cardPoints):
            total=total-cardPoints[r]+cardPoints[l]
            maxSum=max(maxSum,total)
            l+=1
            r+=1
        return maxSum
