n = int(input())
visited = set()
count = 0
for i in range(n):
    row = list(map(int, input().split()))

    for j in range(len(row)):
        if row[j] == 1:
            if (i, j) not in visited:
                count += 1
                visited.add((i, j))
                visited.add((j, i))
print(count)
