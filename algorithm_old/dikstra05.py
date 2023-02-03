import heapq

n, m = map(int, input().split())

def dikstra(graph, n):
    INF = 1e9
    dist = [INF]*(n+1)

    dist[1] = 0
    q = []
    heapq.heappush(q, (dist[1], 1))
    while q:
        accu_dist, node = heapq.heappop(q)
        for adj in graph[node]:
            if dist[adj] > accu_dist + 1:
                dist[adj] = accu_dist + 1
                heapq.heappush(q, (dist[adj], adj))


    max_value = max(dist[1:])
    max_number = 0
    same_count = 0
    for i in range(1, n+1):
        if dist[i] == max_value:
            same_count += 1
            if max_number == 0:
                max_number = i

    print(max_number, max_value, same_count)


graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dikstra(graph, n)
