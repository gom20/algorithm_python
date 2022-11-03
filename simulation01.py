# L R U D

def isValid(x, y, d, n):
    if d == 'R' and x == 5:
        return False
    elif d == 'L' and x == 1:
        return False
    elif d == 'U' and y == 1:
        return False
    elif d == 'D' and y == 5:
        return False
    return True

n = map(int, input().split())
arr = list(input().split())

x = 1
y = 1

for i in range(len(arr)):
    dir = arr[i]
    if isValid(x, y, dir, n):
        if dir == 'L' :
            x -= 1
        elif dir == 'R':
            x += 1
        elif dir == 'U':
            y -= 1
        elif dir == 'D':
            y += 1

print(y, x)



