import heapq
n, m, c = map(int, input().split())
INF = 1e9
distance = [INF]*(n+1)
distance[c] = 0
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

def dikstra(graph, distance, start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for adj in graph[now]:
            node = adj[0]
            cost = adj[1]
            if (dist + cost) < distance[node]:
                distance[node] = dist + cost
                heapq.heappush(q, (dist+cost, node))

dikstra(graph, distance, c)
print(distance)
city_cnt = 0
total_time = 0
for city in distance:
    if city == INF or city == 0:
        continue
    city_cnt += 1
    total_time = max(total_time, city)

print(total_time)