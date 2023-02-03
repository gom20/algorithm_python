xs = []
ys = []

for i in range(0, 3):
    x1, y1 = map(int, input().split())
    xs.append(x1)
    ys.append(y1)

def setCnt(list, dic):
    for x in list:
        if not x in dic.keys():
            dic[x] = 1
        else:
            dic[x] = dic[x] + 1

xdic = {}
ydic = {}
setCnt(xs, xdic)
setCnt(ys, ydic)

new_x = ""
new_y = ""
for key, value in xdic.items() :
    if value == 1:
        new_x = key

for key, value in ydic.items() :
    if value == 1:
        new_y = key

print(new_x, new_y)