n, m = map(int, input().split())
x, y, d = map(int, input().split())
# 북동남서 0 1 2 3
step = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = [[False]*m for _ in range(n)]
visited[x][y] = True

def test(x, y, d):
    global n, m, visited

    # 네 방향 모두 가본 좌표 인지 확인
    b_possible = False
    for i in range(4):
        nx = x + step[i][0]
        ny = y + step[i][1]
        if arr[nx][ny] == 0 and not visited[nx][ny]:
            b_possible = True
            break

    if b_possible:
        # 왼쪽 방향 전진 좌표 확인
        # 왼쪽 방향 회전
        nd = d + 1 if d + 1 <= 3 else 0
        nx = x + step[nd][0]
        ny = y + step[nd][1]
        if not visited[nx][ny]:
            visited[nx][ny] = True
            test(nx, ny, nd)
        else:
            test(x, y, nd)
    else:
        nx = x + step[d][0]*-1
        ny = y + step[d][1]*-1
        if arr[nx][ny] == 1:
            count = 0
            for i in range(n):
                for j in range(m):
                    if visited[i][j]:
                        count += 1
            print(count)
            exit(0)
        else:
            test(nx, ny, d)

arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

test(x, y, d)