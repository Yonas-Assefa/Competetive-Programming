n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))

left = 0
right = 0
tempSum = 0
count = 0
while right < n:
    tempSum += arr[right]

    while tempSum >= s:
        count += (n - right)
        tempSum -= arr[left]
        left += 1
        
    right += 1
print(count)