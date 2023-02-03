str = input()

rs = int(str[0])
for s in str[1:]:
    num = int(s)
    if rs == 0:
        rs += num
    else:
        if num == 0:
            rs += num
        else:
            rs *= num

print(rs)
