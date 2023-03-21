n, m = list(map(int, input().split()))
power = list(map(int, input().split()))
power.sort()
ans = 0
left = 0
right = n - 1
temp = power[right]

while left < right:
    if temp > m:
        ans += 1
        right -= 1
        temp = power[right]
    else:
        temp += power[right]
        left += 1
    
if temp > m:
    ans += 1
print(ans) 



