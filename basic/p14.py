n = int(input())
arr = []
for _ in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))

arr.sort(key = lambda s : s[1])

for a in arr:
    print(a[0], end = ' ')