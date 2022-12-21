from itertools import combinations
import copy
from collections import deque
n, m = map(int, input().split())
center = []
for i in range(n):
    row = list(map(int, input().split()))
    center.append(row)

blanks = []
viruses = []
for i in range(n):
    for j in range(m):
        if center[i][j] == 0:
            blanks.append((i, j))
        elif center[i][j] == 2:
            viruses.append((i, j))

answer = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(start, temp):
    sx, sy = start
    que = deque()
    que.append((sx, sy))

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or temp[nx][ny] != 0:
                continue
            temp[nx][ny] = 2
            que.append((nx, ny))

combi = combinations(blanks, 3)
for added_walls in combi:
    temp_center = copy.deepcopy(center)

    for wall in added_walls:
        wx, wy = wall
        temp_center[wx][wy] = 1

    for virus in viruses:
        bfs(virus, temp_center)

    zero_cnt = 0

    for i in range(n):
        for j in range(m):
            if temp_center[i][j] == 0:
               zero_cnt += 1
    answer = max(answer, zero_cnt)

print(answer)