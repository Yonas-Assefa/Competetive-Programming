test = int(input())
ans = []

for _ in range(test):
    n = int(input())
    monster = list(map(int, input().split()))
    monster.sort()
    if n == 1:
        ans.append(1)
    elif n == 2:
        one = 0
        two = 1
        
        if monster[one] == 1 and monster[two] == 1:
            ans.append(1)
        else:
            ans.append(2)
    else:
        ones = 0
        for i in range(n):
            if monster[i] == 1:
                ones += 1
            else:
                break
        if ones %2 == 0:
            count = ones // 2 + (n - ones)
            ans.append(count)
        else:
            count = ones // 2 + (n - ones + 1)
            ans.append(count)
for i in ans:
    print(i)





