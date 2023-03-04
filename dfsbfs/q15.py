from collections import deque
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

INF = 1e9
dist = [INF]*(n+1)

def bfs(start):
    q = deque()
    q.append((x, 0))
    dist[x] = 0
    while q:
        node, acc_cost = q.popleft()
        for adj_node in graph[node]:
            if dist[adj_node] > acc_cost + 1:
                q.append((adj_node, acc_cost + 1))
                dist[adj_node] = acc_cost + 1

bfs(x)

result = []
for i in range(1, n+1):
    if dist[i] == k:
        result.append(i)

result.sort()

if len(result) == 0:
    print(-1)
else:
    for rs in result:
        print(rs)