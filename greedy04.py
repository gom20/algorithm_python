str = input()

zero_cnt = 0
one_cnt = 0
flag = False
if str[0] == '1':
    flag = True
    one_cnt += 1
else:
    zero_cnt += 1

for s in str[1:]:
    if flag == True and s == '0':
        zero_cnt += 1
        flag = False
    elif flag == False and s == '1':
        one_cnt += 1
        flag = True

print(min(zero_cnt, one_cnt))