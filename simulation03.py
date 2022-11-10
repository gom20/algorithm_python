#a1

global cnt
cnt = 0

def isValid(num):
    if num >= 9 or num < 1:
        return False
    else:
        return True

def move(x, y):
    parallelMove(x, y, True, True)
    parallelMove(x, y, True, False)
    verticalMove(x, y, True, True)
    verticalMove(x, y, True, False)

def parallelMove(x, y, isFirst, isRight):
    global cnt
    if isFirst:
        if isRight:
            nx = x+2
        else:
            nx = x-2
        if not isValid(nx):
            return
        verticalMove(nx, y, False, True)
        verticalMove(nx, y, False, False)
    else:
        if isRight:
            nx = x+1
        else:
            nx = x-1
        if not isValid(nx):
            return
        cnt += 1

def verticalMove(x, y, isFirst, isDown):
    global cnt
    if isFirst:
        if isDown:
            ny = y+2
        else:
            ny = y-2
        if not isValid(ny):
            return
        parallelMove(x, ny, False, True)
        parallelMove(x, ny, False, False)
    else:
        if isDown:
            ny = y+1
        else:
            ny = y-1
        if not isValid(ny):
            return
        cnt += 1

str = list(input())
dic = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}
x = dic.get(str[0])
y = int(str[1])

move(x, y)
print(cnt)
