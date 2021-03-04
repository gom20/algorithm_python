x, y, w, h = map(int, input().split())
print(min(min(x, w-x), min(y, h-y)))
