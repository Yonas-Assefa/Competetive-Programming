n, m = list(map(int, input().split()))
arr1 =list(map(int, input().split()))
arr2 = list(map(int, input().split()))

#logic
ans = [0] * m
top = 0
botm = 0
while botm < m:
    while (top < n) and (arr1[top] < arr2[botm]):
        top += 1

    ans[botm] = top
    botm += 1
print(*ans, sep=" ")

