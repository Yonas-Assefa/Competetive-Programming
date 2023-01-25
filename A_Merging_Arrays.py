n, m = map(int, input().split(" "))
n_list = list(map(int, input().split(" ")))
m_list = list(map(int, input().split(" ")))

ans = []
upper = 0
lower = 0

while upper < n and lower < m:
    if n_list[upper] <= m_list[lower]:
        ans.append(n_list[upper])
        upper += 1
    else:
        ans.append(m_list[lower])
        lower += 1

if upper == n:
    ans += m_list[lower: ]
else:
    ans += n_list[upper: ]


print(*ans, sep = " ")



