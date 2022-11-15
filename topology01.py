# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4


from collections import deque
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
in_degree = [0]*(v+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1


que = deque()
for i in range(1, len(in_degree)):
    if in_degree[i] == 0:
        que.append(i)

while que:
    now = que.popleft()
    print(now)
    for adj in graph[now]:
        in_degree[adj] -= 1
        if in_degree[adj] == 0:
            que.append(adj)
