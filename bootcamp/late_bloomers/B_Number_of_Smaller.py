n, m = list(map(int, input().split()))
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

ans = []
count = 0

point1 = 0
point2 = 0

while point1 < n and point2 < m:

    while point1 < n and list2[point2] > list1[point1]:
        count += 1
        point1 += 1

    ans.append(count)
    point2 += 1
    # print(ans)
    # print(point1, point2)
while len(ans) < m:
    ans.append(ans[-1])
    
print(*ans, sep = " ")