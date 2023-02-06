test_case = int(input())
ans = []

for i in range(test_case):
    seq_leng = int(input())
    seq = list(map(int, input().split()))
    left = 0
    right = seq_leng - 1
    res = []
    while left < right:
        res.append(seq[left])
        res.append(seq[right])
        left += 1
        right -= 1
    if left == right:
        res.append(seq[left])
        
    ans.append(res)

for i in ans:
    print(*i, sep=" ")
