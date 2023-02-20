# N개 도시
# 단방향
# C에서 출발

import heapq

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range (m):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))

INF = 1e9
dist = [INF]*(n+1)
dist[c] = 0

q = []
heapq.heappush(q, (0, c))

while q:
    distance, node = heapq.heappop(q)
    if distance > dist[node]:
        continue
    for adj in graph[node]:
        cost, adj_node = adj
        if distance + cost < dist[adj_node]:
            dist[adj_node] = distance + cost
            heapq.heappush(q, (dist[adj_node], adj_node))

print(dist)
# 도달할 수 있는 도시 개수
# 총 걸리는 시간
time = 0
count = 0
for i in range(1, n+1):
    if dist[i] != INF and i != c:
        count += 1
        time = max(time, dist[i])

print(count, time, end= ' ')