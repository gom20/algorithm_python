# 2 15
# 2
# 3

n, m = map(int, input().split())
values = []
for i in range(n):
    values.append(int(input()))
values.sort(reverse=True)

dp = [0]*(m+1)
for i in range(min(values), m+1):
    for value in values:
        if i == value:
            dp[i] = 1
            break
        elif i % value == 0:
            dp[i] = dp[i//value] + (i//value)
            break

print(dp[m] if not dp[m] == 0 else -1)
