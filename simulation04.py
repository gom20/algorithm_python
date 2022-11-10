n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = []
# 북, 동, 남, 서
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)

arr[x][y] = 2
cnt = 1

def lotate(cx, cy, cd):
    global cnt
    # 왼쪽 방향 회전
    nd = cd - 1
    nd = nd if nd >= 0 else 3

    # 네 방향 체크
    if not isPossible(cx, cy):
        # 이동 가능한 칸이 없다면?
        nx = cx + dirs[nd][0]*-1
        ny = cy + dirs[nd][1]*-1
        if arr[nx][ny] == 1:
            # 현재 방향에서 뒷칸이 바다일 경우 종료
            print(cnt)
            exit(1)
        else:
            # 현재 방향 뒷칸에서 다시 1단계 실행
            lotate(nx, ny, nd)
    else:
        # 이동 가능한 칸이 있다면?
        nx = cx + dirs[nd][0]
        ny = cy + dirs[nd][1]
        if valid(nx, ny):
            # 유효한 칸인가?
            # 유효한 칸이라면 해당 칸으로 이동하여 다시 1단계 실행
            arr[nx][ny] = 2
            cnt += 1
            lotate(nx, ny, nd)
        else:
            # 유효한 칸이 아니면 현재 위치에서 다시 1단계 실행
            lotate(cx, cy, nd)

def isPossible(x, y):
    for dir in dirs:
        nx = x + dir[0]
        ny = y + dir[1]
        if valid(nx, ny):
            return True
    return False

def valid(x, y):
    if x < 0 or x >= 4:
        return False
    if y < 0 or y >= 4:
        return False
    if arr[x][y] != 0:
        return False
    return True

lotate(x, y, d)
