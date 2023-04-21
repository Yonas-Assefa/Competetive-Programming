n = int(input())
ans = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    adj = list(map(int, input().split()))
    for j in range(1, len(adj)):
        dest = adj[j] - 1
        ans[i][dest] = 1
print(ans)


