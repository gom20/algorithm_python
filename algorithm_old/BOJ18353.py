n = int(input())

arr = list(map(int, input().split()))
arr.reverse()
# print(arr)

dp = [1]*n

for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], 1 + dp[j])

print(n-max(dp))

