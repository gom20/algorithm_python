str = input()

left, right = 0, 0
for i in range(len(str)):
    if i < int(len(str)/2):
        left += int(str[i])
    else:
        right += int(str[i])

if left == right:
    print('LUCKY')
else:
    print('READY')