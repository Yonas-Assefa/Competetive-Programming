def max_sum(arr, k):
    n = len(arr)
    maxSum = -1 * float("inf")
    for i in range(n - k + 1):
        total =  0
        for j in range(i , i + k):
            total += arr[j]
        maxSum = max(maxSum,total)
    
    # left = 0
    # right = k
    # n = len(arr)
    # maxSum = -1 * float("inf")
    # while right <= n:
    #     maxSum = max(maxSum, sum(arr[left:right]))
    #     left +=1
    #     right += 1

    return maxSum


print(max_sum([0,1,3,2,1,5],3))
