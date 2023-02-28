n, m = list(map(int, input().split()))
arr1 =list(map(int, input().split()))
arr2 = list(map(int, input().split()))

#logic
top = 0
botm = 0
ans = 0

while top < n and botm < m:
    if arr1[top] == arr2[botm]:
        val = arr1[top]
        countTop = 0
        countBotm = 0

        while top < n and arr1[top] == val:
            countTop += 1
            top += 1
        
        while botm < m and arr2[botm] == val:
            countBotm += 1
            botm += 1
        
        ans += (countBotm * countTop)
    
    elif arr1[top] < arr2[botm]:
        top += 1
    else:
        botm += 1

print(ans)

        

