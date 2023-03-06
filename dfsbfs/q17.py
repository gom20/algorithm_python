import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, k = map(int, input().split())
graph = [[0]*n for _ in range(n)]


q = []


for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        graph[i][j] = row[j]
        if row[j] != 0:
            # virus
            heapq.heappush(q, (row[j], (i, j)))
s, x, y = map(int, input().split())

time = 0
print(q)

while True:
    next_viruses= []
    while q:
        vtype, (vx, vy) = heapq.heappop(q)
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] != 0:
                continue
            graph[nx][ny] = vtype
            next_viruses.append((vtype, (nx, ny)))

    for next_virus in next_viruses:
        heapq.heappush(q, next_virus)

    time += 1
    if len(q) == 0 or time == s:
        print(graph[x-1][y-1])
        break


