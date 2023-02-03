from collections import deque
import sys
input = sys.stdin.readline

# n노드, m간선, k최단거리, x시작노드
n, m, k, x = map(int, input().rstrip().split())

graph = [[] for _ in range(n+1)]
# 간선 정보 입력 받기

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(graph, start, k):
    result = []
    visited = [False] * (n + 1)
    que = deque()
    visited[start] = True
    que.append((start, 0))

    while que:
        now, dist = que.popleft()
        flag = True if dist == k-1 else False
        for adj in graph[now]:
            if visited[adj]:
                continue
            else:
                visited[adj] = True
                if flag:
                    result.append(adj)
                else:
                    que.append((adj, dist + 1))

    if len(result) == 0:
        print(-1)
    else:
        result.sort()
        for r in result:
            print(r)

bfs(graph, x, k)