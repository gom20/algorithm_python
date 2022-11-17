from collections import deque
import heapq

n, k = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
q = []
for i in range(1, n+1):
    data = list(map(int, input().split()))
    for j in range(1, n+1):
        arr[i][j] = data[j-1]
        if data[j-1] != 0:
            # virus
            heapq.heappush(q, (data[j-1], i, j))

# viruses.sort()
s, a, b = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if s == 0:
    print(arr[a][b])
    exit(0)

time = 0
next_viruses = []
while len(q) > 0:
    t, x, y = heapq.heappop(q)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= 0 or ny <= 0 or nx > n or ny > n or arr[nx][ny] != 0:
            continue
        arr[nx][ny] = t
        next_viruses.append((t, nx, ny))

    if len(q) == 0:
        time += 1
        if time == s:
            print(arr[a][b])
            exit(0)
        for virus in next_viruses:
            heapq.heappush(q, virus)
        next_viruses = []

print(arr[a][b])
exit(0)