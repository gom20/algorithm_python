n = int(input())
INF = 30001
dp = [INF]*(n+1)

dp[1] = 0

for i in range(1, n+1):
    count = dp[i] + 1
    if i+1 <= n:
        dp[i+1] = min(dp[i+1], count)
    if i*2 <= n:
        dp[i*2] = min(dp[i*2], count)
    if i * 3 <= n:
        dp[i*3] = min(dp[i*3], count)
    if i * 5 <= n:
        dp[i*5] = min(dp[i*5], count)


print(dp[n])