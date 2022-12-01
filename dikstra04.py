import heapq

t = int(input())
def dikstra(arr, n):
    INF = 1e9
    dist = [[INF]*n for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    dist[0][0] = arr[0][0]
    start = (dist[0][0], 0, 0)
    q = []
    heapq.heappush(q, start)

    while q:
        accu_dist, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if dist[nx][ny] > accu_dist + arr[nx][ny]:
                dist[nx][ny] = accu_dist + arr[nx][ny]
                heapq.heappush(q, (dist[nx][ny], nx, ny))

    return dist[n-1][n-1]

for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    print(dikstra(arr, n))
