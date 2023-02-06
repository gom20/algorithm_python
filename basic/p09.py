# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque
n, m = map(int, input().split())

fx, fy = n-1, m-1
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

answer = 0
def dfs():
    global graph, answer
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    sx, sy, scnt= 0, 0, 1
    queue = deque([(sx, sy, scnt)])

    while queue:
        x, y, cnt = queue.popleft()
        graph[x][y] = 2 # visited

        if x == fx and y == fy:
            print(cnt)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            ncnt = cnt + 1
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] != 1:
                continue
            queue.append((nx, ny, ncnt))



dfs()
