n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))

left = 0
right = 0
tempSum = 0
minLen = n + 1

while right < n:
    tempSum += arr[right]

    while tempSum >= s:
        minLen = min(minLen, right - left + 1)
        tempSum -= arr[left]
        left += 1
        
    right += 1

if minLen > n:
    print(-1)
else:
    print(minLen)

