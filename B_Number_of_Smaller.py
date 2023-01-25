n, m = map(int, input().split(" "))
n_elem = list(map(int, input().split(" ")))
m_elem = list(map(int, input().split(" ")))

less_count = 0
left = 0
ans = []

for i in m_elem:
   
    while left < n and n_elem[left] < i:
        less_count += 1
        left += 1

    ans.append(less_count)

print(*ans, sep = " ")
