num1, num2 = list(map(int, input().split()))
n = int(input())
common = []
first = 2
while first * 2 <= num1:
    if num1 % first == 0 and num2 % first == 0:
        common.append(first)
    first += 1
common.append(num1)
ans  = []
for i in range(n):
    st, end = list(map(int, input().split()))
    res = []
    for i in common:
        if st <= i and end >= i:
            res.append(i)
        # if i > end:
        #     break
    if not res:
        ans.append([-1])
    else:
        ans.append(res)

for i in ans:
    print(*i, sep=" ")
        
