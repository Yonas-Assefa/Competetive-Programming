ans = []
test_case = int(input())

for i in range(test_case):
    seq_len = int(input())
    seq = list(map(int, input().split()))

    left = 0
    right = 0
    res = []

    while right < seq_len:
        max_num = seq[left]

        while right < seq_len and (seq[left] * seq[right]) > 0:
            max_num = max(max_num, seq[right])
            right += 1

        res.append(max_num)
        left = right
    ans.append(sum(res))

for i in ans:
    print(i)
