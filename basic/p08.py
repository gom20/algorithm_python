from collections import deque

n, m = map(int, input().split())

ice = [[0]*m for _ in range(n)]
for i in range(n):
    s = input()
    for j in range(len(s)):
        ice[i][j] = int(s[j])

dxys = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def bfs(sx, sy):
    global ice
    queue = deque([(sx, sy)])

    while queue:
        x, y = queue.popleft()
        ice[x][y] = 1

        for dxy in dxys:
            nx = x + dxy[0]
            ny = y + dxy[1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or ice[nx][ny] == 1:
                continue
            queue.append((nx, ny))

count = 0

for i in range(n):
    for j in range(m):
        if ice[i][j] == 0:
            count += 1
            bfs(i, j)

print(count)