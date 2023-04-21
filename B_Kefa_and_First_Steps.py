inp = int(input())
income = list(map(int, input().split()))
ans = 0
left = 0
right = 0

while right < len(income) - 1:
    if income[right] <= income[right + 1]:
        right += 1

    else:
        ans =  max(ans, (right - left + 1))
        right += 1
        left = right

ans = max(ans, (right - left + 1))
print(ans)
   