test = int(input())

ans = []
for i in range(test):
    n, k = list(map(int, input().split()))
    res = 0
    cur = 0
    while k > 0:
        if k % 2 != 0:
            res += n ** cur

        k = k >> 1
        cur += 1
    res = res % ((10 ** 9) + 7)
    ans.append(res)

for i in ans:
    print(i)

