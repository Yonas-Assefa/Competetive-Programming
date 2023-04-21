test = int(input())
ans = []

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    oddCount = []
    for i in arr:
         if i %2 == 0:
            oddCount.append(i)
    

for i in ans:
     print(ans)
