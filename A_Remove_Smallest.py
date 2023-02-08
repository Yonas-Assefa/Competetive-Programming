test_case = int(input())
ans = []

for _ in range(test_case):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        for j  in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    res = "YES"
    for i in range(n - 1):
        if arr[i] < (arr[i + 1] - 1):
            res = "NO"
            break
    ans.append(res)

for resp in ans:
    print(resp)

