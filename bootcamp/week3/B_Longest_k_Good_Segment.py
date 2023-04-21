n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

left = 0
right = 0
dic = {}
maxLen = 0
ans = []
while right < n:
    dic[arr[right]] = dic.get(arr[right], 0) + 1
    while len(dic) > k:
        dic[arr[left]] = dic[arr[left]] - 1
        if dic[arr[left]] == 0:
            del dic[arr[left]]
        left += 1

    if (right - left + 1) >= maxLen:
        maxLen = right - left + 1
        ans = []
        ans.append(left + 1)
        ans.append(right + 1)   
    right += 1

print(ans[0],ans[1]) 


