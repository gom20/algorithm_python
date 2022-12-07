n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
for i in range(n):
    data = input()
    for j in range(len(data)):
        arr[i][j] = int(data[j])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global arr
    arr[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 1:
            continue
        dfs(nx, ny)

count = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            count += 1
            dfs(i, j)

print(count)