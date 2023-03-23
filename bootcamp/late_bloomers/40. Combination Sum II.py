class Solution(object):
    def combinationSum2(self, candidates, target):
        ans=[]
        n=len(candidates)
        candidates.sort()
        def solve(idx,lst,sum):
            
            if sum==target:
                ans.append(lst)
                return 
            for i in range(idx,n):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if sum+candidates[i]>target:
                    break
                solve(i+1,lst+[candidates[i]],sum+candidates[i])
        solve(0,[],0)
        return ans