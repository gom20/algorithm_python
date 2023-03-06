# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X
# T 선생, S 학생, O 장애물
# 벽 3개 설치해서 모두 감시를 피할 수 있는지 체크

from itertools import combinations

n = int(input())
graph = [['X']*n for _ in range(n)]

teachers = []
o_candidates = []

for i in range(n):
    row = list(input().split())
    for j in range(n):
        graph[i][j] = row[j]
        if row[j] == 'X':
            o_candidates.append((i, j))
        elif row[j] == 'T':
            teachers.append((i, j))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(sx, sy, dir):
    # 0, 1, 2, 3 => 상 하 좌 우
    nx = sx + dx[dir]
    ny = sy + dy[dir]
    if not (nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 'O'):
        if graph[nx][ny] == 'S':
            return True
        else:
            return dfs(nx, ny, dir)
    return False

o_combs = list(combinations(o_candidates, 3))


for walls in o_combs:
    for wall in walls:
        wx, wy = wall
        graph[wx][wy] = 'O'

    # 로직
    possible = True
    for teacher in teachers:
        tx, ty = teacher
        for i in range(4):
            if dfs(tx, ty, i):
                possible = False

    if possible:
        print('YES')
        exit(0)

    for wall in walls:
        wx, wy = wall
        graph[wx][wy] = 'X'

print('NO')