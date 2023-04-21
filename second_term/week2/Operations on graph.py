from collections import defaultdict

no_vertex = int(input())
no_operation = int(input())

graph = defaultdict(list)

for _ in range(no_operation - 1):
    oper = list(map(int, input().split()))
    if oper[0] == 1:
        u = oper[1]
        v = oper[2]
        graph[u].append(v)
        graph[v].append(u)
        
    elif oper[0] == 2:
        oper, vertx = list(map(int, input().split()))
        if graph[vertx]:
            resp = graph[vertx]
            print(*i, sep=" ")
        