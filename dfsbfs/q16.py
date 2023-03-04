from itertools import combinations
from collections import deque


n, m = map(int, input().split())
lab = [[0]*(m+1) for _ in range(n+1)]
dir = [(-1, 0),(1, 0), (0, 1), (0, -1)]

blanks = []
viruses = []
for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, m+1):
        lab[i][j] = row[j-1]
        if lab[i][j] == 0:
            blanks.append((i, j))
        elif lab[i][j] == 2:
            viruses.append((i, j))


def get_safearea(arr):
    safe_area = 0
    for a in range(1, n+1):
        for b in range(1, m+1):
            if arr[a][b] == 0:
                safe_area += 1
    return safe_area

def bfs(arr, node):
    q = deque()
    q.append(node)

    while q:
        x, y = q.popleft()
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx <= 0 or ny <= 0 or nx > n or ny > m or arr[nx][ny] == 2 or arr[nx][ny] == 1:
                continue
            arr[nx][ny] = 2
            q.append((nx, ny))


result = 0
combs = list(combinations(blanks, 3))

for comb in combs:
    for position in comb:
        wx, wy = position
        lab[wx][wy] = 1

    for virus in viruses:
        bfs(lab, virus)

    result = max(result, get_safearea(lab))

    #원상복구
    for position in comb:
        wx, wy = position
        lab[wx][wy] = 0


print(result)