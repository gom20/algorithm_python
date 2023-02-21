# 위상 정렬

from collections import deque

n, m = map(int, input().split())
in_degree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    # a -> b
    in_degree[b] +=1
    graph[a].append(b)

q = deque()
for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)


result = []
while q:
    node = q.popleft()
    result.append(node)
    for adj in graph[node]:
        in_degree[adj] -= 1
        if in_degree[adj] == 0:
            q.append(adj)


print(result, end= ' ')