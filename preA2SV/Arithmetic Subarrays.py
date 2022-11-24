class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ansLst=[]
        for i in range(len(l)):
            j=0
            k=1
            srtLst=sorted(nums[l[i]:r[i]+1])
            preDiff=srtLst[k]-srtLst[j]
            ans=True
            while k<len(srtLst):
                if srtLst[k]-srtLst[j]!= preDiff:
                    ans=False
                j+=1
                k+=1

            ansLst.append(ans)
        return ansLst
