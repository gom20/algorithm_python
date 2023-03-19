n = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, len(row)+1):
        graph[i][j] = row[j-1]


dp[1][1] = graph[1][1]
for i in range(2, n+1):
    for j in range(1, i+1):
        if j == 1:
            dp[i][j] = max(graph[i][j] + dp[i-1][j], dp[i][j])
        elif j == i:
            dp[i][j] = max(graph[i][j] + dp[i-1][j-1], dp[i][j])
        else:
            dp[i][j] = max(graph[i][j] + dp[i-1][j], dp[i][j], graph[i][j] + dp[i-1][j-1], dp[i][j])


print(max(dp[n]))