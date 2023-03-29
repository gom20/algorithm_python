n, m = map(int, input().split())
INF = 1e9
graph = [[INF]*(n+1) for _ in range(n+1)]


for a in range(1, n+1):
    for b in range(1, n+1):
        if 1 == b:
            graph[a][b]  = 0

for _ in range(n):
    a, b = map(int, input().split())
    # a < b
    graph[a][b] = 1


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print(graph)
answer = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    print(count)
    if count == n-1:
        answer += 1

print(answer)