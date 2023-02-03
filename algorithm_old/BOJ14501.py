n = int(input())
t, p = [0]*n, [0]*n

for i in range(n):
    t[i], p[i] = map(int, input().split())

#dp[i]는 i일부터 마지막날까지 얻을수 있는 최대 상담 이윤

max_value = 0
dp = [0]*(n+1)
for i in range(n-1, -1, -1):
    if i + t[i] <= n:
        max_value = max(p[i] + dp[i+t[i]], max_value)
        dp[i] = max_value
    else:
        dp[i] = max_value

print(max_value)