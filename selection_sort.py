#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            k=arr[i]
            smallIndex=i
            for j in range(i+1,n):
                if arr[smallIndex]<arr[j]:
                    smallIndex=j
            arr[i],arr[smallIndex]=arr[smallIndex],arr[i]
        arr.reverse()
        
