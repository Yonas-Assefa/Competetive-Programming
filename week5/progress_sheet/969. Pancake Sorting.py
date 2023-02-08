class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)

        for i in range(n):
            maxIndex = 0

            for j in range(n - i):
                if arr[j] > arr[maxIndex]:
                    maxIndex = j

            if maxIndex != (n - 1 - i):
                
                if maxIndex != 0:
                    ans.append(maxIndex + 1)
                    ans.append(n - i)
                    arr[:maxIndex + 1] = arr[maxIndex::-1]
                    arr[:(n - i)] = arr[(n - i) -1 ::-1]

                else:
                    ans.append(n - i)
                    arr[:n - i] = arr[n - i -1 ::-1]
    
        return ans