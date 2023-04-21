test = int(input())
ans = []
for _ in range(test):
    rooms = int(input())
    evils = list(map(int, input().split()))
    res = 0
    left = 0
    while left < rooms and evils[left] == 0:
        left += 1
    
    for i in range(left, rooms - 1):
        if evils[i] == 0:
            res += 1
        else:
            res += evils[i]
    ans.append(res)

for i in ans:
    print(i)