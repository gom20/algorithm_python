n = input()

result = 0
for i in range(len(n)):
    if i < len(n)//2:
        result += int(n[i])
    else:
        result -= int(n[i])

if result == 0:
    print('LUCKY')
else:
    print('READY')