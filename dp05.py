n = int(input())

array = [[0]*n for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        array[i][j] = data[j]


dp = [[0]*n for _ in range(n)]
dp[0][0] = array[0][0]
for i in range(1, n):
    for j in range(0, n):
        if j == 0:
            dp[i][j] = array[i][j] + dp[i-1][j]
        if j == n-1:
            dp[i][j] = array[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i-1][j])

max_value = 0
for i in range(n):
    max_value = max(dp[n-1][i], max_value)

print(max_value)