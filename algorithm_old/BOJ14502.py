from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())

center = [[0] * (m+1) for _ in range(n+1)]
viruses = []
blanks = []

direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
answer = 0

def bfs(center, viruses):
    global answer

    que = deque()
    # 초기 바이러스
    for virus in viruses:
        que.append(virus)

    while que:
        cx, cy = que.popleft()
        for dir in direction:
            nx = cx + dir[0]
            ny = cy + dir[1]
            if nx <= 0 or ny <= 0 or nx > n or ny > m or center[nx][ny] == 1 or center[nx][ny] == 2:
                 continue
            que.append((nx, ny))
            center[nx][ny] = 2

    answer = max(answer, calculate_safetyzone(center))


def calculate_safetyzone(center):
    count = 0
    global n, m
    for i in range(1, n+1):
        for j in range(1, m+1):
            if center[i][j] == 0:
                count += 1
    return count

for i in range(1, n+1):
    data = list(map(int, input().split()))
    for j in range(1, m+1):
        center[i][j] = data[j-1]
        if data[j-1] == 0:
            blanks.append((i, j))
        elif data[j-1] == 2:
            viruses.append((i, j))

# 벽 3개를 세울 좌표 조합을 구해야 함
walls_list = list(combinations(blanks, 3))
for walls in walls_list:
    mock_center = copy.deepcopy(center)

    for wall in walls:
        # 벽 3개 설치
        wx, wy = wall[0], wall[1]
        mock_center[wx][wy] = 1
    bfs(mock_center, viruses)

print(answer)