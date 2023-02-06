l = input()
x = int(l[1])  # 행
y = ord(l[0]) - 96 #열

move =  [[-2, -1], [-2, 1], [2, 1],[2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
count = 0

for m in move:
    nx =  x + m[0]
    ny  = y + m[1]
    if nx <= 0 or ny <= 0 or nx > 8 or ny > 8:
        continue
    count += 1

print(count)