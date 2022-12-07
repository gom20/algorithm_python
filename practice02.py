#왕실의 나이트
n = 8
location = input()
x = int(location[1])
y = ord(location[0]) - ord('a') + 1

dxy = [[(0, 2), (0, -2), [(1, 0), (-1, 0)]], [(2, 0), (-2, 0), [(0, 1), (0, -1)]]]
count = 0
for first in dxy:
    for i in range(2):
        fx = x + first[i][0]
        fy = y + first[i][1]
        for second in first[2]:
            nx = fx + second[0]
            ny = fy + second[1]
            if nx > 0 and ny > 0 and nx <= n and ny <= n:
                count += 1

print(count)