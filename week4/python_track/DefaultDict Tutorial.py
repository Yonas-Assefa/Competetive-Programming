# Enter your code here. Read input from STDIN. Print output to STDOUT
#input
n, m = map(int, input().split(" "))

group_A = []
group_B = []
for i in range(n):
    group_A.append(input())

for j in range(m):
    group_B.append(input())

#logic
from collections import defaultdict
group_A_dict = defaultdict(lambda: [])

for i in range(n):
    book = group_A[i]
    group_A_dict[book].append(i + 1)
for book in group_B:
    A_copy = group_A_dict[book]
    if A_copy:
        print(*A_copy, sep = " ")
    else:
        print(-1)



