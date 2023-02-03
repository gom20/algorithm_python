n = int(input())
arr = list(map(int, input().split()))

#f(i) = max(f(i-1), f(i-2)+k)

dp = [0]*n
dp[0] = arr[0]
dp[1] = arr[1]
dp[2] = max(dp[0], dp[1]+arr[2])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i])

print(dp[n-1])
