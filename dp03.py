n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

INF = 10001
dp = [INF]*(m+1)
dp[0] = 10001
for i in arr:
    for j in range(i, m+1):
        if dp[j] == INF and dp[j-i] == INF:
            if j%i == 0:
                dp[j] = j//i
        else:
            dp[j] = min(dp[j], dp[j-i]+1)

result = dp[m]
if dp[m] == INF:
    result = -1

