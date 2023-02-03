from collections import deque

n = int(input())
arr = [[0]*n for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
x, y, size = 0, 0, 2

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 9:
            x, y = i, j
            arr[i][j] = 0
        else:
            arr[i][j] = data[j]

def is_fish(ix, iy, isize):
    global arr, n
    for i in range(n):
        for j in range(n):
            if i == ix and j == iy:
                continue
            if 0 < arr[i][j] < isize:
                return True
    return False

def bfs(sx, sy, ssize, visited):
    global n, arr
    arr[sx][sy] = 0
    que = deque()
    que.append((sx, sy, ssize, 0))
    visited[sx][sy] = True

    while que:
        qx, qy, qsize, qtime = que.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny] or arr[nx][ny] > qsize:
                continue
            if arr[nx][ny] <= qsize:
                if arr[nx][ny] == qsize or arr[nx][ny] == 0:
                    visited[nx][ny] = True
                    que.append((nx, ny, qsize, qtime + 1))
                elif arr[nx][ny] < qsize:
                    print('eat: ', nx, ny)
                    return qtime+1, nx, ny
    return None


eat_cnt, total_time = 0, 0
fx, fy, fsize = x, y, size
while True:
    if is_fish(fx, fy, fsize):
        print(fx, fy, fsize)
        visited = [[False]*n for _ in range(n)]
        result = bfs(fx, fy, fsize, visited)
        if result is None:
            break
        ftime, fx, fy = result
        arr[fx][fy] = 0
        eat_cnt += 1
        if eat_cnt == fsize:
            print('>>>>>>>>>>>')
            fsize += 1
            eat_cnt = 0
        total_time += ftime
    else:
        break

print(total_time)