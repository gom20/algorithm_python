n = int(input())

info = {'R': [0, 1], 'L': [0, -1], 'U' : [-1, 0], 'D': [1, 0]}
dir_arr = list(input().split())

y, x = 1, 1
for d in dir_arr:
    dy, dx = info.get(d)
    if x + dx < 1 or x + dx > n or y + dy < 1 or y + dy > n:
        continue
    x += dx
    y += dy

print(y, x)
