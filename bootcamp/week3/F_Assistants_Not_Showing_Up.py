n, m = list(map(int, input().split()))
set1 = set()

for i in range(m):
    st, end = list(map(int, input().split()))
    temp = set(range(st, end + 1))
    set1.update(temp)

if len(set1) < n:
    print("YES")
else:
    print( 'NO')
