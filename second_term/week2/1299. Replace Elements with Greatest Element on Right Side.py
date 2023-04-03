class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0 for _ in range(n)]
        curMax = -1

        for i in range(n - 1 , -1 , -1):
            ans[i] = curMax
            if arr[i] > curMax:
                curMax = arr[i]
            print(curMax, i)
        
        return ans
                


                