n = int(input())
count = 0
for  i in range(1, n + 1):
    ans = set()
    d = 2
    while d * d < i:

        while i % d <= 0:
            ans.add(d)
            i //= d
        d += 1
        
    if i > 1:
        ans.add(i)

    if len(ans) == 2:
        count += 1
        
print(count)

