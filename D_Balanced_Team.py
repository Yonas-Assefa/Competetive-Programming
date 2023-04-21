test = int(input())
stud = list(map(int, input().split()))
ans = 0
left = 0
right = 0
while right < test - 1:
    diff = stud[right] - stud[right +1]
    if diff < 0 :
        diff = diff * -1
    if diff <= 5:
        right += 1
    else:
        ans = max(ans, (right - left + 1))
        right += 1
        left  = right

ans = max(ans, (right - left + 1))
print(ans)