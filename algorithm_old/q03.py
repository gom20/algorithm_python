s = input()

zero_cnt = 0
one_cnt = 0
prev = s[0]
for i in range(1, len(s)):
    if s[i] != prev:
        if s[i] == '1':
            zero_cnt +=1
        else:
            one_cnt += 1
        prev = s[i]

print(min(zero_cnt, one_cnt))