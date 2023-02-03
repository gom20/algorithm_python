import sys

sys.setrecursionlimit(10**5)

n, l, r = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
checked = [[False]*n for _ in range(n)]

def dfs(board, union, checked, x, y):
    checked[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or checked[nx][ny]:
            continue
        if l <= abs(board[x][y] - board[nx][ny]) <= r:
            union.append((nx, ny))
            dfs(board, union, checked, nx, ny)

day = 0
while True:
    unions = []
    checked = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not checked[i][j]:
                union = [(i, j)]
                dfs(board, union, checked, i, j)
                unions.append(union)

    # board 인구수 업데이트
    if len(unions) == n*n:
        break
    else:
        day += 1
        for union in unions:
            people_count = 0
            for nation in union:
                x, y = nation
                people_count += board[x][y]
            updated_count = int(people_count//len(union))
            for nation in union:
                x, y = nation
                board[x][y] = updated_count

print(day)