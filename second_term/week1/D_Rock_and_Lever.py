import math

test = int(input())

ans = []
for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse = True)
    count  = 0
    for i in range(n):
        num1 = arr[i]
        for j in range(i + 1, n):
            num2 = arr[j]
            exp1 = int(math.log(num1, 2))
            exp2 = int(math.log(num2, 2))
            if exp1 - exp2 > 0:
                 break
            count += 1
        
    ans.append(count)

for i in ans:
    print(i)



