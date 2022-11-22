n = int(input())
m = int(input())

arr = [[1e9]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            arr[i][j] = 0

for _ in range(m):
    i, j, cost = map(int, input().split())
    arr[i][j] = min(arr[i][j], cost)

for k in range(1 ,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(1, n+1):

    for j in range(1, n+1):
        if arr[i][j] == 1e9:
            arr[i][j] = 0
        print(arr[i][j], end= ' ')
    print()