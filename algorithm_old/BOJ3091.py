from collections import deque

n = int(input())
k = int(input())
dummy_map = [[0]*(n+1) for _ in range(n+1)]

# 사과 셋팅
for _ in range(k):
    a, b = map(int, input().split())
    dummy_map[a][b] = 1

# 방향 전환 정보 저장
dir_que = deque()
d = int(input())
for _ in range(d):
    x, dir = input().split()
    dir_que.append((int(x), dir))

# 뱀의 궤적 큐 생성
dummy_map[1][1] = 2
snake_que = deque()
snake_que.append((1, 1))


# 다음 위치가 유효한지 체크
def isValid(a, b):
    if a > n or b > n or a == 0 or b == 0:
        return False
    if dummy_map[a][b] == 2:
        return False
    return True

# 뱀의 방향
N, E, S, W = 0, 1, 2, 3
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cur_dir = E

x = 0
a, b = 1, 1
while x <= 10000:
    x += 1
    a = a + move[cur_dir][0]
    b = b + move[cur_dir][1]

    if isValid(a, b):
        # 사과가 있는지 체크
        if dummy_map[a][b] == 0:
            # 사과가 없으면? 꼬리 지우고 머리 위치 입력
            tail = snake_que.popleft()
            dummy_map[tail[0]][tail[1]] = 0
            snake_que.append((a, b))
            dummy_map[a][b] = 2
        else:
            # 사과가 있으면?
            snake_que.append((a, b))
            dummy_map[a][b] = 2

        # 방향 전환
        if dir_que and x == dir_que[0][0]:
            dir_info = dir_que.popleft()
            if dir_info[1] == 'L':
                cur_dir = cur_dir - 1 if cur_dir >= 1 else 3
            else:
                cur_dir = cur_dir + 1 if cur_dir <= 2 else 0
    else:
        # 벽이나 몸체를 만났을 경우
        print(x)
        break


