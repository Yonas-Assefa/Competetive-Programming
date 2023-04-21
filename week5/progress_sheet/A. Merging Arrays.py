n, m = list(map(int, input().split()))
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
ans = []

top = 0
botm = 0
while top < n and botm < 0:
    if list1[top] < list2[botm]:
        ans.append(list1[top])
        top += 1
    else:
        ans.append(list2[botm])
        botm += 1

ans += list1[top: ]
ans += list2[botm: ]
print(*ans, sep=" ")