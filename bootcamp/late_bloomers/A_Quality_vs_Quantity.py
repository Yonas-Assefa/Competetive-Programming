test = int(input())
ans = []

for _ in range(test):
    n = int(input())
    paint = list(map(int, input().split()))

    paint.sort()
    blue = sum(paint[:2])
    red = paint[n - 1]
    left = 1
    right = n - 1
    flag = False

    while left < right:
        if (red > blue) and (n - right < left + 1):
            ans.append("YES")
            flag = True
            break

        left += 1
        right -= 1
        blue += (paint[left])
        red += paint[right]


    
    # if (red > blue) and (n - right < left + 1):
    #         ans.append("YES")
    if not flag:
        ans.append("NO")
    
for i in ans:
     print(i)
