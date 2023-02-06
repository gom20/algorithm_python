n, m = map(int, input().split())
x, y, d  = map(int, input().split())
move = [[-1, 0], [0, -1], [1, 0], [0, 1]]

answer = 0

gmap = [[0]*m for _ in range(n)]
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(m):
        gmap[i][j] = arr[j]

print(gmap)

gmap[x][y] = 2
answer += 1
while True:
    # 현재 위치에서 왼쪽 방향
    if d+1 > 3:
        d = 0
    else:
        d = d+1

    # 바로 왼쪽 방향에 가보지 않은 칸이 있는 경우만 전진
    nx = x + move[d][0]
    ny = y + move[d][1]
    if 0 <= nx < n and 0 <= ny < m and gmap[nx][ny] == 0:
        gmap[nx][ny] = 2
        answer += 1
        x = nx
        y = ny
        print(x, y)

    # 네 방향 체크
    isPossible = False
    for mv in move:
        nx = x + mv[0]
        ny = y + mv[1]
        if 0 <= nx < n and 0 <= ny < m and gmap[nx][ny] == 0:
            isPossible = True
            break

    # 네 방향 모두 불가능
    if not isPossible:
        nx = x + move[d][0]*-1
        ny = y + move[d][1]*-1
        if 0 <= nx < n and 0 <= ny < m and gmap[nx][ny] == 1:
            print(answer)
            exit(1)
        x = nx
        y = ny




