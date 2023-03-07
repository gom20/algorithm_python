# N개 여행지
n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, n+1):
        graph[i][j] = row[j-1]

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1

plan = list(map(int, input().split()))
for i in range(len(plan)-1):
    if graph[plan[i]][plan[i+1]] == 0:
        print('NO')
        exit(0)

print('YES')