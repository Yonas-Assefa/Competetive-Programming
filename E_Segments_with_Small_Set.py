n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
count = 0
valDict = {}
left = 0
right = 0
dup = 0
while right < n:       
    valDict[arr[right]] = valDict.get(arr[right], 0) + 1    
    while len(valDict) > k:
        valDict[arr[left]] -= 1
        if valDict[arr[left]] == 0:
            del valDict[arr[left]]
        
        left += 1

    count += (right - left + 1 )
    right += 1

print(count - dup)

