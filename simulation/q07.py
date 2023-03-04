#123403

n = input()

r = 0
l = 0
for i in range(len(n)):
    if i < len(n)/2:
        l += int(n[i])
    else:
        r += int(n[i])

if l == r:
    print('LUCKY')
else:
    print('READY')
