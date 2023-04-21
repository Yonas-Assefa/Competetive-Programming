n = int(input(()))
ans = []
for i in range(n):
    row = list(map(int, input().split()))
    adjRow = []
    for j in range(len(row)):
        if row[j] == 1:
            adjRow.append( str(j + 1))
            
    res = str(len(adjRow)) + " " + " ".join(adjRow)
    ans.append(res)

for i in ans:
    print(i)