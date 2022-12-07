from collections import deque

n, m = map(int, input().split())
graph = [[0]*m for _ in range(n)]
for i in range(n):
    data = input()
    for j in range(m):
        graph[i][j] = int(data[j])


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(sx, sy):
    que = deque()
    graph[sx][sy] = 0
    que.append((sx, sy, 1))

    while que:
        x, y, cnt = que.popleft()
        if x == n - 1 and y == m - 1:
            print(cnt)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 0:
                continue
            graph[nx][ny] = 0
            que.append((nx, ny, cnt+1))


bfs(0, 0)