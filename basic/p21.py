import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())
dist = [1e9]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    node, adj, cost = map(int, input().split())
    graph[node].append((adj, cost))

q = []
dist[start] = 0
heapq.heappush(q, (0, start))

while q:
    info = heapq.heappop(q)
    acc_dist = info[0]
    node = info[1]
    if dist[node] < acc_dist:
        continue
    for adj_node in graph[node]:
        if dist[adj_node[0]] <= acc_dist + adj_node[1]:
            continue
        dist[adj_node[0]] = acc_dist + adj_node[1]
        heapq.heappush(q, (acc_dist + adj_node[1], adj_node[0]))


print(dist)

