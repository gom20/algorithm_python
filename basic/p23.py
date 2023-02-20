# 1~N 번 회사
# A는 1번 회사
# X번 회사에 방문
# 양방향 1만큼의 시간
# 1번 -> K번 회사 -> X번 회사


n, m = map(int, input().split())

INF = 1e9
floyd = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            floyd[i][j] = 0


for _ in range(m):
    a, b = map(int, input().split())
    floyd[a][b] = 1
    floyd[b][a] = 1


X, K = map(int, input().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])



if floyd[1][K] or floyd[K][X] == INF:
    print(-1)
else:
    print(floyd[1][K] + floyd[K][X])