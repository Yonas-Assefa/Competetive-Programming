n = int(input())
graph1 = [[] for _ in range(n + 1)]
graph2 = [[] for _ in range(n + 1)]

for i in range(n):
    num = list(map(int, input().split()))
    for j in range(n):
        if num[j] == 1:
            graph1[i].append(j)
            graph2[j].append(i)

sink, source = [], []
for i in range(n):
    if graph1[i] == []:
        sink.append(i + 1)

    if graph2[i] == []:
        source.append(i + 1)

print(len(source), *source)
print(len(sink), *sink)