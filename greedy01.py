n, k = map(int, input().split())

rs = 0
mok = n
while True:
    if mok == 1:
        break
    elif mok % k == 0:
        mok = mok/k
        rs += 1
    else:
        mok -= 1
        rs += 1

print(rs)