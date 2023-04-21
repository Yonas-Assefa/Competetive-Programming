n, k , q = list(map(int, input().split()))
ans = []
temp = []
for t in range(n):
    min, max = list(map(int, input().split()))
    temp.append(min)
    temp.append(max)

set1 = set(temp)
temp_list = list(set1)
temp_list.sort()
print(temp_list)
for que in range(q):
    min, max = list(map(int, input().split()))
    res = 0
    print(min, max)
    if (min in set1) and( max in set1):
        res = max - min
    ans.append(res)
for an in ans:
    print(an)




