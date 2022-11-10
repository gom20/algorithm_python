from collections import deque

n, m = map(int, input().split())
endX, endY = n-1, m-1

dist = []
graph = []


for i in range(n):
    data = list(input())
    graph.append(data)
    dist.append([0] * m)

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, d):
    if x == endX and y == endY:
        print(d)
        exit(1)

    queue = deque()
    dist[x][y] = d
    graph[x][y] = '2'

    for d in direction:
        nx = x + d[0]
        ny = y + d[1]
        nd = dist[x][y] + 1
        if n > nx >= 0 and m > ny >= 0 and graph[nx][ny] == '1':
            queue.append((nx, ny, nd))

    while queue:
        data = queue.popleft()
        nx = data[0]
        ny = data[1]
        nd = data[2]
        bfs(nx, ny, nd)

bfs(0, 0, 1)