#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        minIndex = i
        n = len(arr)
        for j in range(i, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        return minIndex
            
    
    def selectionSort(self, arr,n):
        for i in range(n):
            minIndex = self.select(arr, i)
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr
            
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends