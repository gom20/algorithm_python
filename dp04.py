t = int(input())


dxy = [(0, 1), (-1, 1), (1, 1)]

def dfs(x, y, arr, value, dp, n, m):
    global dxy
    if arr[x][y] + value > dp[x][y]:
        dp[x][y] = arr[x][y] + value
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < n and 0 <= ny < m:
                dfs(nx, ny, arr, dp[x][y], dp, n, m)


def solution(n, m, arr):
    dp = [[0]*m for _ in range(n)]

    for i in range(n):
        dfs(i, 0, arr, 0, dp, n, m)

    max_value = 0
    for i in range(n):
        max_value = max(dp[i][m-1], max_value)
    return max_value


for _ in range(t):
    n, m = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    data = list(map(int, input().split()))
    idx = 0
    for i in range(n):
        for j in range(m):
            arr[i][j] = data[idx]
            idx += 1

    print(solution(n, m, arr))