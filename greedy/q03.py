# 001100
# 1110011

s = input();
zeroCnt =0;
oneCnt = 0;

n = s[0];
if n == 1:
    oneCnt += 1
else:
    zeroCnt += 1

for i in range(1, len(s)):
    if n != s[i]:
        if s[i] == '1':
            oneCnt += 1
        else:
            zeroCnt += 1
        n = s[i]

print(min(oneCnt, zeroCnt))