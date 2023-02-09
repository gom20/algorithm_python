n = int(input())
m = int(input())

graph = [[1e9]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost

for i in range(1, n+1):
    graph[i][i] = 0


for k in range(1, n+1):
    for b in range(1, n+1):
        for a in range(1, n+1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == 1e9:
            print("INFINITY", end= " ")
        else:
            print(graph[a][b], end = " ")
    print()