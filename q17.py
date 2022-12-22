import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, k = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

q = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        graph[i+1][j+1] = data[j]
        if data[j] != 0:
            heapq.heappush(q, (data[j], i+1, j+1))

s, x, y = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
t = 0
next_viruses = []

while t < s and q:
    while q:
        virus, vx, vy = heapq.heappop(q)
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0 or nx > n or ny > n or graph[nx][ny] != 0:
                continue
            graph[nx][ny] = virus
            next_viruses.append((virus, nx, ny))

    for virus in next_viruses:
        heapq.heappush(q, virus)
    next_viruses = []
    t += 1


print(graph[x][y])