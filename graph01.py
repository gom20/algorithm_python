n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
for i in range(n):
    row = input()
    for j in range(0, len(row)):
        arr[i][j] = int(row[j])

direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]
def dfs(x, y):
    arr[x][y] = 1
    for d in direction:
        nx = x + d[0]
        ny = y + d[1]
        if n > nx >= 0 and m > ny >= 0 and arr[nx][ny] == 0:
            dfs(nx, ny)

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            dfs(i, j)
            cnt += 1

print(cnt)