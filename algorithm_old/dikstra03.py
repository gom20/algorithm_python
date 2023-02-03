import heapq
import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))

def dikstra(start):
    INF = int(1e9)
    dist = [INF for _ in range(n+1)]

    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist[now] < dist:
            continue
        for adj in graph[now]:
            cost = dist + adj[1]
            if dist[adj[0]] > cost:
                dist[adj[0]] = cost
                heapq.heappush(q, (cost, adj[0]))

    rs = 0
    for d in dist[1:]:
        if d != 0 and d!= INF:
            rs += 1
    print(rs, max(dist[1:]))

dikstra(c)


